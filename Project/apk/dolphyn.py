import time


def cmd():
    frames = [
        r"""
        
                 ;'-. 
    `;-._        )  '---.._
      >  `-.__.-'          `'.__
     /_.-'-._         _,   ^ ---)
     `       `'------/_.'----``` 
    """,
        r"""
                     ;'-. 
        `;-._        )  '---.._
          >  `-.__.-'          `'.__
         /_.-'-._         _,   ^ ---)
         `       `'------/_.'----``` 
    """,
        r"""
                         ;'-. 
            `;-._        )  '---.._
              >  `-.__.-'          `'.__
             /_.-'-._         _,   ^ ---)
             `       `'------/_.'----``` 
    """,
        r"""
                             ;'-. 
                `;-._        )  '---.._
                  >  `-.__.-'          `'.__
                 /_.-'-._         _,   ^ ---)
                 `       `'------/_.'----```  
    """,
        r"""
                                 ;'-. 
                    `;-._        )  '---.._
                      >  `-.__.-'          `'.__
                     /_.-'-._         _,   ^ ---)
                     `       `'------/_.'----```
    """,
        r"""
                                     ;'-. 
                        `;-._        )  '---.._
                          >  `-.__.-'          `'.__
                         /_.-'-._         _,   ^ ---)
                         `       `'------/_.'----```  
    """,
        r"""
                                         ;'-. 
                            `;-._        )  '---.._
                              >  `-.__.-'          `'.__
                             /_.-'-._         _,   ^ ---)
                             `       `'------/_.'----```  
    """,
        r"""
                                             ;'-. 
                                `;-._        )  '---.._
                                  >  `-.__.-'          `'.__
                                 /_.-'-._         _,   ^ ---)
                                 `       `'------/_.'----```  
    """,
        r"""
                                                 ;'-. 
                                    `;-._        )  '---.._
                                      >  `-.__.-'          `'.__
                                     /_.-'-._         _,   ^ ---)
                                     `       `'------/_.'----```  
    """,
        r"""
                                                     ;'-. 
                                        `;-._        )  '---.._
                                          >  `-.__.-'          `'.__
                                         /_.-'-._         _,   ^ ---)
                                         `       `'------/_.'----```  
    """,
        r"""
                                                         ;'-. 
                                            `;-._        )  '---.._
                                              >  `-.__.-'          `'.__
                                             /_.-'-._         _,   ^ ---)
                                             `       `'------/_.'----```  
    """,
        r"""
                                                             ;'-. 
                                                `;-._        )  '---.._
                                                  >  `-.__.-'          `'.__
                                                 /_.-'-._         _,   ^ ---)
                                                 `       `'------/_.'----```  
    """,
        r"""
                                                                 ;'-. 
                                                    `;-._        )  '---.._
                                                      >  `-.__.-'          `'.__
                                                     /_.-'-._         _,   ^ ---)
                                                     `       `'------/_.'----```  
    """,
        r"""
                                                                     ;'-. 
                                                        `;-._        )  '---.._
                                                          >  `-.__.-'          `'.__
                                                         /_.-'-._         _,   ^ ---)
                                                         `       `'------/_.'----```  
    """,
        r"""
                                                                         ;'-. 
                                                            `;-._        )  '---.._
                                                              >  `-.__.-'          `'.__
                                                             /_.-'-._         _,   ^ ---)
                                                             `       `'------/_.'----```  
    """,
        r"""
                                                                             ;'-. 
                                                                `;-._        )  '---.._
                                                                  >  `-.__.-'          `'.__
                                                                 /_.-'-._         _,   ^ ---)
                                                                 `       `'------/_.'----```  
    """,
        r"""
                                                                                 ;'-. 
                                                                    `;-._        )  '---.._
                                                                      >  `-.__.-'          `'.__
                                                                     /_.-'-._         _,   ^ ---)
                                                                     `       `'------/_.'----```  
    """,
        r"""
                                                                                     ;'-. 
                                                                        `;-._        )  '---.._
                                                                          >  `-.__.-'          `'.__
                                                                         /_.-'-._         _,   ^ ---)
                                                                         `       `'------/_.'----```  
    """,
        r"""
                                                                                         ;'-. 
                                                                            `;-._        )  '---.._
                                                                              >  `-.__.-'          `'.__
                                                                             /_.-'-._         _,   ^ ---)
                                                                             `       `'------/_.'----```  
    """,
        r"""
                                                                                             ;'-. 
                                                                                `;-._        )  '---.._
                                                                                  >  `-.__.-'          `'.__
                                                                                 /_.-'-._         _,   ^ ---)
                                                                                 `       `'------/_.'----```  
    """,
        r"""
                                                                                                 ;'-. 
                                                                                    `;-._        )  '---.._
                                                                                      >  `-.__.-'          `'.__
                                                                                     /_.-'-._         _,   ^ ---)
                                                                                     `       `'------/_.'----```  
    """,
        r"""
                                                                                                     ;'-. 
                                                                                        `;-._        )  '---.._
                                                                                          >  `-.__.-'          `'.__
                                                                                         /_.-'-._         _,   ^ ---)
                                                                                         `       `'------/_.'----```  
    """,
    ]

    for frame in frames:
        print("\033[34m" + frame)
        time.sleep(0.4)
        print("\033[H\033[J" + "\033[0m")
