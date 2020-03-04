# LT2212 V20 Assignment 2

Put any documentation here including any answers to the questions in the 
assignment on Canvas.

For the tokenzation of the corpus, i built a pipeline that first lowercased all words and then checked whether all characters in the word are alphabetical (isalpha()). I later removed all features from the array that had less than overall 5 counts, recucing them to 21560 features(words).

Part 4:

Reduction: TruncatedSVD

KNeighborsClassifier(5):
100%: accuracy:  0.33687002652519893 , precision:  0.6018310856095513 , recall:  0.33687002652519893 , F1 score:  0.38032315099492653
50%:  accuracy:  0.35092838196286474 , precision:  0.5967802455512383 , recall:  0.35092838196286474 , F1 score:  0.3912572552021133
25%:  accuracy:  0.39389920424403185 , precision:  0.6003696855584256 , recall:  0.39389920424403185 , F1 score:  0.43393224689893073
10%:  accuracy:  0.4326259946949602 , precision:  0.5781104305105386 , recall:  0.4326259946949602 , F1 score:  0.46084780821299337
5%:   accuracy:  0.45384615384615384 , precision:  0.55444286938693 , recall:  0.45384615384615384 , F1 score:  0.47229356936430233

The system with the KNeighbours Classifier performed the worst when given the full 21560 features, improving the fewer dimensions the input had. Only one aspect, the precision was actually better when given more features, and decreasing with the reduced dimensions.

DecisionTreeClassifier:
100%: accuracy:  0.5862068965517241 , precision:  0.5873905502134584 , recall:  0.5862068965517241 , F1 score:  0.585655162795387
50%:  accuracy:  0.17718832891246683 , precision:  0.1761429599463199 , recall:  0.17718832891246683 , F1 score:  0.17615331148314953
25%:  accuracy:  0.18779840848806367 , precision:  0.18868736301926642 , recall:  0.18779840848806367 , F1 score:  0.18785266209217524
10%:  accuracy:  0.19946949602122016 , precision:  0.20191709400398639 , recall:  0.19946949602122016 , F1 score:  0.20024406537452816
5%:   accuracy:  0.21193633952254642 , precision:  0.2118806433605718 , recall:  0.21193633952254642 , F1 score:  0.21151159626510685

The system with the Decision Tree Classifier performed the best in all aspects, when given the full amount of features. When reduced to 50%, it performed drastically worse, actually the worst out of all the tests. When reducing the dimensions further the performance improved slightly.

Part Bonus:

Reduction: PCA

KNeighborsClassifier(5):
100%: accuracy:  0.343236074270557 , precision:  0.6018811764456717 , recall:  0.343236074270557 , F1 score:  0.38447237869621886
50%:  accuracy:  0.35172413793103446 , precision:  0.5991663512244892 , recall:  0.35172413793103446 , F1 score:  0.3925475202003058
25%:  accuracy:  0.3941644562334218 , precision:  0.6015704154563255 , recall:  0.3941644562334218 , F1 score:  0.43428400346182605
10%:  accuracy:  0.43448275862068964 , precision:  0.5798953599576648 , recall:  0.43448275862068964 , F1 score:  0.46249869205224087
5%:   accuracy:  0.45225464190981435 , precision:  0.5519132706950972 , recall:  0.45225464190981435 , F1 score:  0.47068273240975655

DecisionTreeClassifier:
100%: accuracy:  0.5949602122015916 , precision:  0.5968639299228997 , recall:  0.5949602122015916 , F1 score:  0.5945886804997446
50%:  accuracy:  0.1883289124668435 , precision:  0.19092419121313847 , recall:  0.1883289124668435 , F1 score:  0.18910949535451096
25%:  accuracy:  0.19787798408488064 , precision:  0.19792347304571106 , recall:  0.19787798408488064 , F1 score:  0.19741280841272046
10%:  accuracy:  0.21326259946949602 , precision:  0.21329015413165342 , recall:  0.21326259946949602 , F1 score:  0.2128478676933174
5%:   accuracy:  0.21326259946949602 , precision:  0.2131063087996847 , recall:  0.21326259946949602 , F1 score:  0.21294986266779908


The values are overall a little bit higher when using PCA, but it seems that the impact of the dimensionality reductor was relativly small. The differences were bigger when using the Decision Tree classifiert, than with the KNeighbours Classifier.

