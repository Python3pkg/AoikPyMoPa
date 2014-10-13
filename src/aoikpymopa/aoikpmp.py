# coding: utf-8
"""
File ID: 7gnhLqN
"""

import sys
import traceback

def get_traceback_txt():
    #/
    exc_cls, exc_obj, tb_obj = sys.exc_info()
    
    #/
    txt_s = traceback.format_exception(exc_cls, exc_obj, tb_obj)

    #/
    res = ''.join(txt_s)

    return res

def main():
    #/ 3b6Ki0R
    #/ check if one cmd arg is given
    ##
    ## Not use |argparse|, to be runnable on earlier versions.
    if len(sys.argv) != 2:
        #/ 2kvytFw
        #/ print program usage
        print(r'Usage: aoikpmp PYTHON.MODULE.NAME')
        
        #/ 5wy7KfF
        return

    #/ 8mZpbO5
    #/ get module name from cmd arg
    mod_name = sys.argv[1]
    
    #/ 7ebCaw3
    #/ strip
    mod_name = mod_name.strip()
    
    #/ 9ajluft
    #/ check empty
    if not mod_name:
        #/ 5r2BDCr
        print('Module name is empty.')
        
        #/ 4mT4ZAC
        return
    
    #/ 5u275Zi
    try:
        __import__(mod_name)
        
        module_obj = sys.modules[mod_name]
    
    #/ 9uEiknz
    except ImportError:
        #/ 7mh7zq8
        print('Module |%s| can not be imported.' % (mod_name,))
        
        #/ 2u8X5uS
        return
    
    #/ 8chsA3e
    except Exception:
        #/ 3hxMp7X
        print('Module |%s| has had errors when being imported:' % (mod_name,))
        print('---\n%s---' % (get_traceback_txt(),))
        
        #/ 8uesUe7
        return
    
    #/ 5wDCYfz
    file_attr = getattr(module_obj, '__file__', None)
    
    #/ 9mF0Bon
    if file_attr:
        #/ 5cx96oq
        print(module_obj.__file__)
        
        #/ 5sD72KR
        return
    
    assert not file_attr
    
    #/ 6rd9ZQf
    if sys.version_info >= (3,3):
        #/ 3fD2QXv
        path_attr = getattr(module_obj, '__path__', None)
        
        #/ 3ciXNc3
        if path_attr:
            #/ 8ywKbb4
            path_s = getattr(path_attr, '_path', None)
            
            #/ 9vDyznY
            if path_s is not None:
                #/ 6mbxZLa
                for path in path_s:
                    print(path)
                
                #/ 3yzCipE
                return
            
            #/ 4fHaXUt
            assert path_s is None
            
            path_attr_txt = str(path_attr)
            
            #/ 9kLbpP4
            #/ extract path
            if path_attr_txt.startswith("_NamespacePath(['") \
            and path_attr_txt.endswith("'])"): 
            ## e.g. _NamespacePath(['D:\\1\\aaa', 'D:\\2\\aaa'])
               path_attr_txt = path_attr_txt[17:-3]
               
               path_attr_txt = '\n'.join(path_attr_txt.split(r"', '"))
               
               path_attr_txt = path_attr_txt.replace(r'\\', '\\')
               
            #/ 9bTCtcQ
            print(path_attr_txt)
            
            #/ 4adMYkv
            return
        
        #else: 5kyPX75
    #else: 5kyPX75
        
    #/ 5kyPX75
    print("Module |%s| seems to have no file. Is it a built-in?" % (mod_name,))
    
    #/ 7c8lYAJ
    return

if __name__ == '__main__':
    main()
    