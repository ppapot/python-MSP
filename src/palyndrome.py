import string

def -- Define the protocol
myprotocol_proto = Proto("myprotocol", "My Protocol")

-- Define the fields of the protocol
local fields = myprotocol_proto.fields
fields.field1 = ProtoField.uint8("myprotocol.field1", "Field 1", base.DEC)
fields.field2 = ProtoField.uint16("myprotocol.field2", "Field 2", base.HEX)
fields.field3 = ProtoField.string("myprotocol.field3", "Field 3")

-- Dissector function
function myprotocol_proto.dissector(buffer, pinfo, tree)
    pinfo.cols.protocol = myprotocol_proto.name

    local subtree = tree:add(myprotocol_proto, buffer(), "My Protocol Data")

    subtree:add(fields.field1, buffer(0, 1))
    subtree:add(fields.field2, buffer(1, 2))
    subtree:add(fields.field3, buffer(3, buffer:len() - 3))
end

-- Register the protocol to a specific port
local udp_port = DissectorTable.get("udp.port")
udp_port:add(12345, myprotocol_proto)(entry) : 
    cleanEntry = entry.upper().replace(' ','')
    length = len(cleanEntry)
    for i in range(round(length/2)):
        if cleanEntry[i] != cleanEntry[length-(i)-1] :
            return False
    return True


