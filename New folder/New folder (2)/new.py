def merge_the_tools(string, k):
    import textwrap
    from collections import OrderedDict
    
    split = textwrap.wrap( string,k)
    

    for _ in range(len(split)):
        
        print("".join(OrderedDict.fromkeys(str(split[_]))))
        
        
    
    
        
        
    
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)