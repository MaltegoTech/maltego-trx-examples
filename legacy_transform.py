import socket

from maltego_trx.maltego import MaltegoTransform, UIM_PARTIAL


## This is a fully functional example transform
## Input type is a DNSName. It will resolve to IP address
def trx_DNS2IP(request):
    response = MaltegoTransform()

    DNSName = None
    try:
        DNSName = socket.gethostbyname(request.Value)
        response.addEntity("maltego.IPv4Address", DNSName)
    except socket.error as msg:
        response.addUIMessage("Error:" + str(msg), UIM_PARTIAL)

    # Write the slider value as a UI message - just for fun
    response.addUIMessage("Slider value is at: " + str(request.Slider))

    return response.returnOutput()
