// Iterative approach

const countDownIteratively = num => {
  for (let i = num; i > 0; i--) {
    console.log(i);
  }
  console.log('All done');
}

countDownIterativly(10);
/*
10
9
8
7
6
5
4
3
2
1
All done
*/


// Recursive approach

const countDown = num => {
  // base case
  if (num <= 0) {
    console.log('All done');
    return;
  }
  console.log(num);
  num--;
  // self calling
  countDown(num);
}

countDown(10);
/*
10
9
8
7
6
5
4
3
2
1
All done
*/
