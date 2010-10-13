# Python stubs generated by omniidl from server-command-corba.idl

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA

_omnipy.checkVersion(3,0, __file__)


#
# Start of module "CorbaServer"
#
__name__ = "CorbaServer"
_0_CorbaServer = omniORB.openModule("CorbaServer", r"server-command-corba.idl")
_0_CorbaServer__POA = omniORB.openModule("CorbaServer__POA", r"server-command-corba.idl")


# typedef ... DoubleSeq
class DoubleSeq:
    _NP_RepositoryId = "IDL:CorbaServer/DoubleSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CorbaServer.DoubleSeq = DoubleSeq
_0_CorbaServer._d_DoubleSeq  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_double, 0)
_0_CorbaServer._ad_DoubleSeq = (omniORB.tcInternal.tv_alias, DoubleSeq._NP_RepositoryId, "DoubleSeq", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_double, 0))
_0_CorbaServer._tc_DoubleSeq = omniORB.tcInternal.createTypeCode(_0_CorbaServer._ad_DoubleSeq)
omniORB.registerType(DoubleSeq._NP_RepositoryId, _0_CorbaServer._ad_DoubleSeq, _0_CorbaServer._tc_DoubleSeq)
del DoubleSeq

# typedef ... StringStreamer
class StringStreamer:
    _NP_RepositoryId = "IDL:CorbaServer/StringStreamer:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CorbaServer.StringStreamer = StringStreamer
_0_CorbaServer._d_StringStreamer  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_char, 0)
_0_CorbaServer._ad_StringStreamer = (omniORB.tcInternal.tv_alias, StringStreamer._NP_RepositoryId, "StringStreamer", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_char, 0))
_0_CorbaServer._tc_StringStreamer = omniORB.tcInternal.createTypeCode(_0_CorbaServer._ad_StringStreamer)
omniORB.registerType(StringStreamer._NP_RepositoryId, _0_CorbaServer._ad_StringStreamer, _0_CorbaServer._tc_StringStreamer)
del StringStreamer

# typedef ... SeqOfDoubleSeq
class SeqOfDoubleSeq:
    _NP_RepositoryId = "IDL:CorbaServer/SeqOfDoubleSeq:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CorbaServer.SeqOfDoubleSeq = SeqOfDoubleSeq
_0_CorbaServer._d_SeqOfDoubleSeq  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:CorbaServer/DoubleSeq:1.0"], 0)
_0_CorbaServer._ad_SeqOfDoubleSeq = (omniORB.tcInternal.tv_alias, SeqOfDoubleSeq._NP_RepositoryId, "SeqOfDoubleSeq", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:CorbaServer/DoubleSeq:1.0"], 0))
_0_CorbaServer._tc_SeqOfDoubleSeq = omniORB.tcInternal.createTypeCode(_0_CorbaServer._ad_SeqOfDoubleSeq)
omniORB.registerType(SeqOfDoubleSeq._NP_RepositoryId, _0_CorbaServer._ad_SeqOfDoubleSeq, _0_CorbaServer._tc_SeqOfDoubleSeq)
del SeqOfDoubleSeq

# typedef ... SeqOfStringStreamer
class SeqOfStringStreamer:
    _NP_RepositoryId = "IDL:CorbaServer/SeqOfStringStreamer:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CorbaServer.SeqOfStringStreamer = SeqOfStringStreamer
_0_CorbaServer._d_SeqOfStringStreamer  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:CorbaServer/StringStreamer:1.0"], 0)
_0_CorbaServer._ad_SeqOfStringStreamer = (omniORB.tcInternal.tv_alias, SeqOfStringStreamer._NP_RepositoryId, "SeqOfStringStreamer", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:CorbaServer/StringStreamer:1.0"], 0))
_0_CorbaServer._tc_SeqOfStringStreamer = omniORB.tcInternal.createTypeCode(_0_CorbaServer._ad_SeqOfStringStreamer)
omniORB.registerType(SeqOfStringStreamer._NP_RepositoryId, _0_CorbaServer._ad_SeqOfStringStreamer, _0_CorbaServer._tc_SeqOfStringStreamer)
del SeqOfStringStreamer

# typedef ... SeqOfRank
class SeqOfRank:
    _NP_RepositoryId = "IDL:CorbaServer/SeqOfRank:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CorbaServer.SeqOfRank = SeqOfRank
_0_CorbaServer._d_SeqOfRank  = (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0)
_0_CorbaServer._ad_SeqOfRank = (omniORB.tcInternal.tv_alias, SeqOfRank._NP_RepositoryId, "SeqOfRank", (omniORB.tcInternal.tv_sequence, omniORB.tcInternal.tv_long, 0))
_0_CorbaServer._tc_SeqOfRank = omniORB.tcInternal.createTypeCode(_0_CorbaServer._ad_SeqOfRank)
omniORB.registerType(SeqOfRank._NP_RepositoryId, _0_CorbaServer._ad_SeqOfRank, _0_CorbaServer._tc_SeqOfRank)
del SeqOfRank

# interface NotifyCallback
_0_CorbaServer._d_NotifyCallback = (omniORB.tcInternal.tv_objref, "IDL:CorbaServer/NotifyCallback:1.0", "NotifyCallback")
omniORB.typeMapping["IDL:CorbaServer/NotifyCallback:1.0"] = _0_CorbaServer._d_NotifyCallback
_0_CorbaServer.NotifyCallback = omniORB.newEmptyClass()
class NotifyCallback :
    _NP_RepositoryId = _0_CorbaServer._d_NotifyCallback[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CorbaServer.NotifyCallback = NotifyCallback
_0_CorbaServer._tc_NotifyCallback = omniORB.tcInternal.createTypeCode(_0_CorbaServer._d_NotifyCallback)
omniORB.registerType(NotifyCallback._NP_RepositoryId, _0_CorbaServer._d_NotifyCallback, _0_CorbaServer._tc_NotifyCallback)

# NotifyCallback operations and attributes
NotifyCallback._d_notifyClient = ((), (), None)

# NotifyCallback object reference
class _objref_NotifyCallback (CORBA.Object):
    _NP_RepositoryId = NotifyCallback._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def notifyClient(self, *args):
        return _omnipy.invoke(self, "notifyClient", _0_CorbaServer.NotifyCallback._d_notifyClient, args)

    __methods__ = ["notifyClient"] + CORBA.Object.__methods__

omniORB.registerObjref(NotifyCallback._NP_RepositoryId, _objref_NotifyCallback)
_0_CorbaServer._objref_NotifyCallback = _objref_NotifyCallback
del NotifyCallback, _objref_NotifyCallback

# NotifyCallback skeleton
__name__ = "CorbaServer__POA"
class NotifyCallback (PortableServer.Servant):
    _NP_RepositoryId = _0_CorbaServer.NotifyCallback._NP_RepositoryId


    _omni_op_d = {"notifyClient": _0_CorbaServer.NotifyCallback._d_notifyClient}

NotifyCallback._omni_skeleton = NotifyCallback
_0_CorbaServer__POA.NotifyCallback = NotifyCallback
omniORB.registerSkeleton(NotifyCallback._NP_RepositoryId, NotifyCallback)
del NotifyCallback
__name__ = "CorbaServer"

# interface SOT_Server_Command
_0_CorbaServer._d_SOT_Server_Command = (omniORB.tcInternal.tv_objref, "IDL:CorbaServer/SOT_Server_Command:1.0", "SOT_Server_Command")
omniORB.typeMapping["IDL:CorbaServer/SOT_Server_Command:1.0"] = _0_CorbaServer._d_SOT_Server_Command
_0_CorbaServer.SOT_Server_Command = omniORB.newEmptyClass()
class SOT_Server_Command :
    _NP_RepositoryId = _0_CorbaServer._d_SOT_Server_Command[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CorbaServer.SOT_Server_Command = SOT_Server_Command
_0_CorbaServer._tc_SOT_Server_Command = omniORB.tcInternal.createTypeCode(_0_CorbaServer._d_SOT_Server_Command)
omniORB.registerType(SOT_Server_Command._NP_RepositoryId, _0_CorbaServer._d_SOT_Server_Command, _0_CorbaServer._tc_SOT_Server_Command)

# SOT_Server_Command operations and attributes
SOT_Server_Command._d_run = (((omniORB.tcInternal.tv_string,0), ), (), None)
SOT_Server_Command._d_runAndRead = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:CorbaServer/StringStreamer:1.0"], ), None)
SOT_Server_Command._d_readVector = (((omniORB.tcInternal.tv_string,0), ), (omniORB.typeMapping["IDL:CorbaServer/DoubleSeq:1.0"], ), None)
SOT_Server_Command._d_createOutputVectorSignal = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_long, ), None)
SOT_Server_Command._d_createInputVectorSignal = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_long, ), None)
SOT_Server_Command._d_readInputVectorSignal = ((omniORB.tcInternal.tv_long, ), (omniORB.typeMapping["IDL:CorbaServer/DoubleSeq:1.0"], ), None)
SOT_Server_Command._d_readSeqInputVectorSignal = ((omniORB.typeMapping["IDL:CorbaServer/SeqOfRank:1.0"], ), (omniORB.typeMapping["IDL:CorbaServer/SeqOfDoubleSeq:1.0"], ), None)
SOT_Server_Command._d_writeOutputVectorSignal = ((omniORB.tcInternal.tv_long, omniORB.typeMapping["IDL:CorbaServer/DoubleSeq:1.0"]), (), None)
SOT_Server_Command._d_registerClient = ((omniORB.typeMapping["IDL:CorbaServer/NotifyCallback:1.0"], (omniORB.tcInternal.tv_string,0)), (), None)
SOT_Server_Command._d_unregisterClient = (((omniORB.tcInternal.tv_string,0), ), (), None)

# SOT_Server_Command object reference
class _objref_SOT_Server_Command (CORBA.Object):
    _NP_RepositoryId = SOT_Server_Command._NP_RepositoryId

    def __init__(self):
        CORBA.Object.__init__(self)

    def run(self, *args):
        return _omnipy.invoke(self, "run", _0_CorbaServer.SOT_Server_Command._d_run, args)

    def runAndRead(self, *args):
        return _omnipy.invoke(self, "runAndRead", _0_CorbaServer.SOT_Server_Command._d_runAndRead, args)

    def readVector(self, *args):
        return _omnipy.invoke(self, "readVector", _0_CorbaServer.SOT_Server_Command._d_readVector, args)

    def createOutputVectorSignal(self, *args):
        return _omnipy.invoke(self, "createOutputVectorSignal", _0_CorbaServer.SOT_Server_Command._d_createOutputVectorSignal, args)

    def createInputVectorSignal(self, *args):
        return _omnipy.invoke(self, "createInputVectorSignal", _0_CorbaServer.SOT_Server_Command._d_createInputVectorSignal, args)

    def readInputVectorSignal(self, *args):
        return _omnipy.invoke(self, "readInputVectorSignal", _0_CorbaServer.SOT_Server_Command._d_readInputVectorSignal, args)

    def readSeqInputVectorSignal(self, *args):
        return _omnipy.invoke(self, "readSeqInputVectorSignal", _0_CorbaServer.SOT_Server_Command._d_readSeqInputVectorSignal, args)

    def writeOutputVectorSignal(self, *args):
        return _omnipy.invoke(self, "writeOutputVectorSignal", _0_CorbaServer.SOT_Server_Command._d_writeOutputVectorSignal, args)

    def registerClient(self, *args):
        return _omnipy.invoke(self, "registerClient", _0_CorbaServer.SOT_Server_Command._d_registerClient, args)

    def unregisterClient(self, *args):
        return _omnipy.invoke(self, "unregisterClient", _0_CorbaServer.SOT_Server_Command._d_unregisterClient, args)

    __methods__ = ["run", "runAndRead", "readVector", "createOutputVectorSignal", "createInputVectorSignal", "readInputVectorSignal", "readSeqInputVectorSignal", "writeOutputVectorSignal", "registerClient", "unregisterClient"] + CORBA.Object.__methods__

omniORB.registerObjref(SOT_Server_Command._NP_RepositoryId, _objref_SOT_Server_Command)
_0_CorbaServer._objref_SOT_Server_Command = _objref_SOT_Server_Command
del SOT_Server_Command, _objref_SOT_Server_Command

# SOT_Server_Command skeleton
__name__ = "CorbaServer__POA"
class SOT_Server_Command (PortableServer.Servant):
    _NP_RepositoryId = _0_CorbaServer.SOT_Server_Command._NP_RepositoryId


    _omni_op_d = {"run": _0_CorbaServer.SOT_Server_Command._d_run, "runAndRead": _0_CorbaServer.SOT_Server_Command._d_runAndRead, "readVector": _0_CorbaServer.SOT_Server_Command._d_readVector, "createOutputVectorSignal": _0_CorbaServer.SOT_Server_Command._d_createOutputVectorSignal, "createInputVectorSignal": _0_CorbaServer.SOT_Server_Command._d_createInputVectorSignal, "readInputVectorSignal": _0_CorbaServer.SOT_Server_Command._d_readInputVectorSignal, "readSeqInputVectorSignal": _0_CorbaServer.SOT_Server_Command._d_readSeqInputVectorSignal, "writeOutputVectorSignal": _0_CorbaServer.SOT_Server_Command._d_writeOutputVectorSignal, "registerClient": _0_CorbaServer.SOT_Server_Command._d_registerClient, "unregisterClient": _0_CorbaServer.SOT_Server_Command._d_unregisterClient}

SOT_Server_Command._omni_skeleton = SOT_Server_Command
_0_CorbaServer__POA.SOT_Server_Command = SOT_Server_Command
omniORB.registerSkeleton(SOT_Server_Command._NP_RepositoryId, SOT_Server_Command)
del SOT_Server_Command
__name__ = "CorbaServer"

#
# End of module "CorbaServer"
#
__name__ = "server_command_corba_idl"

_exported_modules = ( "CorbaServer", )

# The end.
