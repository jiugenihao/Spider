@echo off

set proto_file = %1
protoc ./Login.proto  --python_out=./

pause