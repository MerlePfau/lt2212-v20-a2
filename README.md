# LT2212 V20 Assignment 2

Put any documentation here including any answers to the questions in the 
assignment on Canvas.

For the tokenzation of the corpus, i built a pipeline that first lowercased all words and then checked whether all characters in the word are alphabetical (isalpha()). I later removed all features from the array that had less than overall 10 counts, recucing them to 15665 features(words).

Part 4:

Reduction: TruncatedSVD

KNeighborsClassifier(5):
100%:  
50%:    
25%:  
10%:  accuracy:  0.3750663129973475 , precision:  0.4028828673081433 , recall:  0.3750663129973475 , F1 score:  0.3762090648886889
5%:   accuracy:  0.36047745358090183 , precision:  0.38323678051048765 , recall:  0.36047745358090183 , F1 score:  0.36028132199715224

The system with the KNeighbours Classifier performed the worst when given the full 15665 features, improving the fewer dimensions the input had. Only one aspect, the precision was actually better when given more features, and decreasing with the reduced dimensions.

DecisionTreeClassifier:
100%: accuracy:  0.5888594164456233 , precision:  0.5916441011308207 , recall:  0.5888594164456233 , F1 score:  0.5890586995774381
50%:  
25%:   
10%:  accuracy:  0.1673740053050398 , precision:  0.16965735460574682 , recall:  0.1673740053050398 , F1 score:  0.16809691554206055
5%:   accuracy:  0.16816976127320954 , precision:  0.17248135436712866 , recall:  0.16816976127320954 , F1 score:  0.1698837177908523

The system with the Decision Tree Classifier performed the best in all aspects, when given the full amount of features. When reduced to 50%, it performed drastically worse, actually the worst out of all the tests. When reducing the dimensions further the performance improved slightly.

Part Bonus:

Reduction: PCA

KNeighborsClassifier(5):
100%: accuracy:  accuracy:  0.37002652519893897 , precision:  0.42037981688167253 , recall:  0.37002652519893897 , F1 score:  0.3767673509211003
50%:  accuracy:  accuracy:  0.37082228116710875 , precision:  0.4162379939823286 , recall:  0.37082228116710875 , F1 score:  0.3768094929635076
25%:  accuracy:  0.37904509283819626 , precision:  0.4167052126389955 , recall:  0.37904509283819626 , F1 score:  0.3827785492351793
10%:  accuracy:  0.37347480106100794 , precision:  0.4014510846490064 , recall:  0.37347480106100794 , F1 score:  0.3750285705307968
5%:   accuracy:  0.36074270557029176 , precision:  0.38341176019627066 , recall:  0.36074270557029176 , F1 score:  0.3604137628092134

DecisionTreeClassifier:
100%: accuracy:  0.5816976127320955 , precision:  0.5827118956493879 , recall:  0.5816976127320955 , F1 score:  0.5811058235956854
50%:  accuracy:  accuracy:  0.14588859416445624 , precision:  0.14870976883967177 , recall:  0.14588859416445624 , F1 score:  0.14689969038267697
25%:  accuracy:  0.1596816976127321 , precision:  0.1613293709915619 , recall:  0.1596816976127321 , F1 score:  0.16009699767849186
10%:  accuracy:  0.16047745358090185 , precision:  0.1624024776455577 , recall:  0.16047745358090185 , F1 score:  0.16112549830322834
5%:   accuracy:  0.17320954907161804 , precision:  0.17400052647324638 , recall:  0.17320954907161804 , F1 score:  0.17330835297430522


The values are overall a little bit higher when using PCA, but it seems that the impact of the dimensionality reductor was relativly small. The differences were bigger when using the Decision Tree classifiert, than with the KNeighbours Classifier.



