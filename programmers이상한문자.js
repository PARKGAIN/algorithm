function solution(s) {
    let answer = '';
    let arr=[];
    arr= s.split(" ") 
    for(let i in arr){
        let ans=arr[i].split("")
        for (let j in ans){
          if(j %2 === 0){
              ans[j] = ans[j].toUpperCase()
          } else{
              ans[j] = ans[j]
          }
        }
       ans= ans.join("")
        //console.log(ans)
    }
   
    console.log(answer)
    //return answer;
}
