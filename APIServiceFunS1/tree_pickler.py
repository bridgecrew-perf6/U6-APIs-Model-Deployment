import pickle # a standard library

# pickling is used for object serialization and
# deserialization
# pickle: save a binary representation of an object
# to a file (for use later...)
# un/depickle: load a binary representation of an
# object from a file (to a python obj in the current
# process)

# imagine PA7... trained a MyDecisionTreeClassifier
# imagine project... trained a MyRandomForestClassifier
# and you want to use these models LATER

# let's do this (pickling/unpickling) for the
# interview_tree_solution
header = ["level", "lang", "tweets", "phd"]
interview_tree_solution =   ["Attribute", "level", 
                                ["Value", "Junior", 
                                    ["Attribute", "phd", 
                                        ["Value", "yes",
                                            ["Leaf", "False", 2, 5]
                                        ],
                                        ["Value", "no",
                                            ["Leaf", "True", 3, 5]
                                        ]
                                    ]
                                ],
                                ["Value", "Mid",
                                    ["Leaf", "True", 4, 14]
                                ],
                                ["Value", "Senior",
                                    ["Attribute", "tweets",
                                        ["Value", "yes",
                                            ["Leaf", "True", 2, 5]
                                        ],
                                        ["Value", "no",
                                            ["Leaf", "False", 3, 5]
                                        ]
                                    ]
                                ]
                            ]

# lets package these two objects into 1
# mytree = MyDecisionTreeClassifier()
# mytree.fit(X_train,  y_train)
packaged_obj = [header, interview_tree_solution]
outfile = open("tree.p", "wb") # binary
pickle.dump(packaged_obj, outfile)
outfile.close()