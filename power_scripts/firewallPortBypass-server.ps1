$rulesIN = Get-NetFirewallRule
    $parIN = @{
    DisplayName = ""
    LocalPort = 80
    Direction="Inbound"
    Protocol ="TCP"
    Action = "Allow"
}


$parIN.LocalPort = 33000
$parIN.DisplayName = "WS Server IN"
if (-not $rulesIN.DisplayName.Contains($parIN.DisplayName)) {New-NetFirewallRule @parIN}


$rulesOUT = Get-NetFirewallRule
    $parOUT = @{
    DisplayName = ""
    LocalPort = 80
    Direction="Outbound"
    Protocol ="TCP"
    Action = "Allow"
}


$parOUT.LocalPort = 33000
$parOUT.DisplayName = "WS Server OUT"
if (-not $rulesOUT.DisplayName.Contains($parOUT.DisplayName)) {New-NetFirewallRule @parOUT}
