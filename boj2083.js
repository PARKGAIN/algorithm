function solution(str) {
  const arr = str.split(" ");
  let ans = "";
  arr[1] > 17 || arr[2] >= 80 ? (ans = "Senior") : (ans = "Junior");
  return ans;
}


