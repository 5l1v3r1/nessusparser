from plugins import genFile

def gen(cb):
	appendices = []

	plugin_ids=["Microsoft Windows SMBv1 Multiple Vulnerabilities"]
	name="Microsoft Windows SMBv1 Support"
	description="Hosts running deployments of Microsoft Windows operating systems each present a Server Message Block (SMB) service which supports connections made using version 1 of the protocol. Several vulnerabilities were identified to affected services configured in such a manner, leaving each host susceptible to various attack vectors."
	risk_description="Each identified Windows host has support for Microsoft Server Message Block 1.0 (SMBv1) enabled. It can be considered vulnerable to multiple issues due to the improper handling of SMBv1 packets and requests. Such issues include information disclosure, denial of service and arbitrary code execution from a remote unauthenticated attacker, all leveraged through crafted SMBv1 packets."
	risk_description+="\n\nThis issue affects all Microsoft Windows Operating System releases, including Windows Server 2016 and Windows 10. It should also be noted that whilst updates have been released for these issues for supported Windows releases, continued use of/support for SMBv1 is not recommended."
	recommendation="Review each host as an authenticated user and ensure the relevant security update for the operating system version present has been applied:"
	recommendation+="\n- Windows Server 2008 : KB4018466"
	recommendation+="\n- Windows 7 : KB4019264"
	recommendation+="\n- Windows Server 2008 R2 : KB4019264"
	recommendation+="\n- Windows Server 2012 : KB4019216"
	recommendation+="\n- Windows 8.1 / RT 8.1. : KB4019215"
	recommendation+="\n- Windows Server 2012 R2 : KB4019215"
	recommendation+="\n- Windows 10 : KB4019474"
	recommendation+="\n- Windows 10 Version 1511 : KB4019473"
	recommendation+="\n- Windows 10 Version 1607 : KB4019472"
	recommendation+="\n- Windows 10 Version 1703 : KB4016871"
	recommendation+="\n- Windows Server 2016 : KB4019472"
	notes="<url>https://support.microsoft.com/help/4016871</url>"
	notes+="\n<url>https://support.microsoft.com/help/4018466</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019213</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019214</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019215</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019216</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019263</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019264</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019472</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019473</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019474</url>"
	notes+="\n<url>https://support.microsoft.com/help/4016871</url>"
	notes+="\n<url>https://support.microsoft.com/help/4018466</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019213</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019214</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019215</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019216</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019263</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019264</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019472</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019473</url>"
	notes+="\n<url>https://support.microsoft.com/help/4019474</url>"

	ap = genFile.genr(cb, plugin_ids, name, description, risk_description, recommendation, notes)
	if not ap is None:
		appendices += ap



	if appendices:
		return appendices