# Add upper toolbar positions in CMC
positions = {
    "st": [(493, 114), (564, 144)],
    "fl": [(493, 114), (559, 172)],
    "conf": [(493, 114), (579, 229)],
    "check": [(412, 108), (482, 241)],
    "reset": [(412, 108), (440, 144)],
    "svc": [(576, 113)],
    "rl": [(1901, 582)],
}

# Add Paths which you want to navigate on host machine in CMC
path_commands = {
    "lp": "%IBERDIR%/LANProxy/LanProxy",
    "temp": "c:\\temp",
    "panda": "c:\\ProgramData\\Panda Security\\Panda Aether Agent\\Downloads",
    "proxyboh": "c:\\CMCLanDesk\\NSS LANProxy",
    "proxyterm": "c:\\CMCLanDesk\\NSS LANProxy Handler",
    "programdata": "c:\\ProgramData",
    "programfiles": "c:\\program files (x86)",
}

# Add commands here that you want to type in CMD of CMC
shell_commands = {
    "pps": 'C:\\temp\\nss\\psinfo.exe -d:"[AETHERUPDATE FULL | LITE]" /nogui',
    "pendpoint": "c:\\temp\\nss\\EndpointAgentTool.exe /cfg /su /s /d /c /ku",
    "psetproxy": "c:\\temp\\nss\\setproxyallusers.bat ",
    "pcertinst": "C:\\Temp\\nss\\CertCheck\\CertCheck /add /ca && C:\\Temp\\nss\\CertCheck\\WESCertcheck /add /ca",
    "pwginst": 'msiexec /i "c:\\temp\\nss\\WatchGuard Agent.msi" /qn /L*V "c:\\temp\\nss\\WatchGuardAgent.log"',
    "checkproxy": "netsh winhttp show proxy",
    "endpoint": "c:\\temp\\EndpointAgentTool.exe /cfg /su /s /d /c /ku",
    "ip": "ipconfig /all",
    "wginst": 'msiexec /i "c:\\temp\\WatchGuard Agent.msi" /qn /L*V "c:\\temp\\WatchGuardAgent.log"',
    "setproxy": "c:\\temp\\setproxyallusers.bat ",
    "wgproxy": "c:\\temp\\wgsetproxyallusers.bat",
    "mkdir": "mkdir c:\\temp",
    "sys": "systeminfo",
    "arp": "arp -a",
    "certinst": "C:\\Temp\\CertCheck\\CertCheck /add /ca && C:\\Temp\\CertCheck\\WESCertcheck /add /ca",
    "lpinst": "%IBERDIR%\\LANProxy\\LANProxy\\InstallLANProxy.bat",
    "ps": 'C:\\temp\\psinfo.exe -d:"[AETHERUPDATE FULL | LITE]" /nogui',
    "tls": "c:\\temp\\tlsfix.exe",
    "lpremove": 'taskkill /f /im lanproxy.exe && sc config lanproxy start= disabled && sc delete lanproxy & rmdir /s /q "%LOCALDIR%\\EPS" & rmdir /s /q "%LOCALDIR%\\LANProxy"',
    "host": "hostname",
    "restart panda": "net stop PandaAetherAgent && net start PandaAetherAgent",
    "sys": "systeminfo",
    "checkbit": 'systeminfo | findstr /i /c:"System Type"',
    "checksha": "systeminfo | findstr KB3140245 & systeminfo | findstr KB4474419",
    "checktls": 'reg query "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\SCHANNEL\\Protocols\\TLS 1.2\\Client"',
    "cleanpanda": 'rmdir /s /q "C:\\Program Files (x86)\\Panda Security" && rmdir /s /q "C:\\ProgramData\\Panda Security"',
    "cleantemp": 'del /q "C:\\temp"',
    "sha1": "wusa.exe c:\\temp\\kb4474419.msu /quiet /norestart /log:c:\\temp\\kb4474419.log",
    "sha2": "wusa.exe c:\\temp\\kb3140245.msu /quiet /norestart /log:c:\\temp\\kb3140245.log",
    "redist32": "C:\\temp\\vcredist2015_2017_2019_2022_x86 /quiet /norestart",
    "redist64": "C:\\temp\\vcredist2015_2017_2019_2022_x64 /quiet /norestart",
    "proxy32term": "c:\\temp\\NSSProxySetup_32bit.exe -device_type=term -host=ALOHABOH -port=9180 -fallback_ip=",
    "proxy64term": "c:\\temp\\NSSProxySetup_64bit.exe -device_type=term -host=ALOHABOH -port=9180 -fallback_ip=",
    "proxy64boh": "c:\\temp\\NSSProxySetup_64bit.exe -device_type=boh -port=9180 -offline",
}
