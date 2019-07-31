var TargetIndex = 300;

var FiboOne = 1;
var FiboTwo = 1;

for (i = 0; i < TargetIndex; i++) {
  var temp = FiboOne + FiboTwo;
  console.log(temp);
  FiboOne = FiboTwo;
  FiboTwo = temp;
}
