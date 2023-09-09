stage1 = ["",         
          "          ",
          "          ",
          "          ",
          "          ",
          "          ",
          " ________ ",
          ] 

stage2 = ["",         
          "          ",
          "|         ",
          "|         ",
          "|         ",
          "|         ",
          "|________ ",
          ] 

stage3 = ["",         
          "______    ",
          "|         ",
          "|         ",
          "|         ",
          "|         ",
          "|________ ",
          ] 

stage4 = ["",         
          "______    ",
          "|    |    ",
          "|         ",
          "|         ",
          "|         ",
          "|________ ",
          ] 

stage5 = ["",         
          "______    ",
          "|    |    ",
          "|    0    ",
          "|         ",
          "|         ",
          "|________ ",
          ]

stage6 = ["",         
          "______    ",
          "|    |    ",
          "|    0    ",
          "|    |    ",
          "|         ",
          "|________ ",
          ]

stage7 = ["",         
          "______    ",
          "|    |    ",
          "|    0    ",
          "|   /|    ",
          "|         ",
          "|________ ",
          ]

stage8 = ["",         
          "______    ",
          "|    |    ",
          "|    0    ",
          "|   /|\   ",
          "|         ",
          "|________ ",
          ]

stage9 = ["",         
          "______    ",
          "|    |    ",
          "|    0    ",
          "|   /|\   ",
          "|   /     ",
          "|________ ",
          ]

stage10 = ["",         
          "______    ",
          "|    |    ",
          "|    0    ",
          "|   /|\   ",
          "|   / \   ",
          "|________ ",
          ]

slownik = {"stage1":stage1,
           "stage2":stage2,
           "stage3":stage3,
           "stage4":stage4,
           "stage5":stage5,
           "stage6":stage6,
           "stage7":stage7,
           "stage8":stage8,
           "stage9":stage9,
           "stage10":stage10}

def slownik(stage):
    slownik = {"stage1":stage1,
           "stage2":stage2,
           "stage3":stage3,
           "stage4":stage4,
           "stage5":stage5,
           "stage6":stage6,
           "stage7":stage7,
           "stage8":stage8,
           "stage9":stage9,
           "stage10":stage10}
    return slownik[stage]

    