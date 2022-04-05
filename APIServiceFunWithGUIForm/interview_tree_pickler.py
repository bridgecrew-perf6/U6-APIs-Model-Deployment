import pickle 

header = ["level", "lang", "tweets", "phd"]
interview_tree = \
    ["Attribute", "level", 
        ["Value", "Senior", 
            ["Attribute", "tweets", 
                ["Value", "yes", 
                    ["Leaf", "True", 2, 5]
                ],
                ["Value", "no", 
                    ["Leaf", "False", 3, 5]
                ]
            ]
        ],
        ["Value", "Mid", 
            ["Leaf", "True", 4, 14]
        ],
        ["Value", "Junior", 
            ["Attribute", "phd", 
                ["Value", "yes", 
                    ["Leaf", "False", 2, 5]
                ],
                ["Value", "no", 
                    ["Leaf", "True", 3, 5]
                ]
            ]
        ]
    ]

# serialize to file (pickle)
outfile = open("tree.p", "wb")
pickle.dump([header, interview_tree], outfile)
outfile.close()

# deserialize to object (unpickle)
infile = open("tree.p", "rb")
header2, interview_tree2 = pickle.load(infile)
infile.close()

# check
print(header2)
print(interview_tree2)