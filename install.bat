@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION
@ECHO ******************************
@ECHO Install the RTE Backend Server
@ECHO ******************************

:: Set the debug level
IF /I "%~3"=="ON" (
    set _debug=ON
    ) ELSE (
    set _debug=OFF
)
@ECHO %_debug%

:: Set variables
SET _reinstall_docker="N"
SET _install

:: Check if configuration is provided
if "%~1"=="" (
    GOTO :DisplayHelp
) else (
    if "%~1"=="-h" (
        GOTO :DisplayHelp
    ) else (
        set _configuration_name="%~1"
    )
)

:: Determine if the Docker container must be reinstalled
if "%~2"=="Y" (
    set _reinstall_docker="Y"
)

:: Set the GITHUB_TOKEN
if %GITHUB_TOKEN%=="" (
    @ECHO The GITHUB_TOKE environment variable is not set.
    set /P _github_token=GitHub Token:
) else (
    set _github_token=%GITHUB_TOKEN%
)

:: Set the variables for the installation
IF /I %_configuration_name%=="docker" (
    CALL :SetDockerConfig
) ELSE IF /I %_configuration_name%=="prod" (
    CALL :SetProdConfig
)

IF /I %_install%==yes (
    GOTO :Install
    ) ELSE (
    GOTO Exit
)

:Install
:: Install the system
IF /I %_reinstall_docker%=="Y" (
    @ECHO ** Rebuild Docker container
    CALL docker-rebuild.bat %_debug%
)
@ECHO ** Setup security
ssh -t -E logs\rte-installbackendserver.log root@%_host% %_port_ssh% "echo 'y' | sudo ufw enable;sudo ufw allow OpenSSH;sudo apt update;sudo apt install openssh-server;sudo ufw allow 22;sudo systemctl start ssh"
@ECHO ** Copy install scripts
scp %_port_scp% src\rte-installbackendserver\rte-installbackendserver_s1.* "%SECRETS_DIR%\env_var.sh" root@%_host%://usr/local/share
@ECHO ** Run install script on the server
ssh -t -E logs\rte-installbackendserver.log root@%_host%  %_port_ssh% "cd /usr/local/share;cd /usr/local/share;bash -x /usr/local/share/rte-installbackendserver_s1.sh rte-installbackendserver_s1.ini %_github_token%"
del "%SECRETS_DIR%\env_var.sh"
GOTO :Exit

:SetDockerConfig
@ECHO Set the Docker variables
SET _host=localhost
SET _port_ssh=-p 2222
SET _port_scp=-P 2222
copy "%SECRETS_DIR%\env_var_dev.sh" "%SECRETS_DIR%\env_var.sh"
SET _install=yes
GOTO :eof

:SetProdConfig
:: DigitalOcean
@ECHO Set the production variables
SET _host=188.166.154.196
SET _port_ssh=-p 22
SET _port_scp=-P 22
copy "%SECRETS_DIR%\env_var_prod.sh" "%SECRETS_DIR%\env_var.sh"
@ECHO "You are about to install the production system.  Are you sure?
set /P _install=Install production (yes/no):
GOTO :eof

:DisplayHelp
@ECHO usage:
@ECHO     install -h
@ECHO     install system reinstall_docker debug
@ECHO where
@ECHO     system: docker / prod
@ECHO     reinstall_docker: Y / N
@ECHO     debug: ON / OFF
@ECHO '
@ECHO Notes:
@ECHO - The GITHUB_TOKEN environment variable must be set.  This token will be used
@ECHO   to clone private repositories
@ECHO - The SECRTES_DIR environment variable must be set. The script with the environment
@ECHO   variable with the passwords and userid's script is located.
GOTO :Exit

:Exit
EXIT /B
