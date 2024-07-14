import asyncio
 
async def read_file():
    with open("./test.txt") as file:
        print(file.read())
 
async def write_file():
    with open("./test.txt", "a+") as file:
        file.write("\nLet's get started.fjkdl;asjfklds;ajfkldsjfkls;djfklds;fjklas;fjksl;fjklsda;jfklsd;ajfkl;sdjkfl;dsjkfl;dsjkfl;sjakfl;sdjfkl;dsjfkl;sdjafkl;dasjkfl;sdjkfl;sdjafklsdajfklsa;f")
 
    
async def main():
    
    ## this code will have race condition error
    ## Enable tracemalloc to get the object allocation traceback
    write_file()
    read_file()
    # await write_file()
    # await read_file()
 
asyncio.run(main())