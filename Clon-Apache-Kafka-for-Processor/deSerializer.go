package main

import (

	"fmt"

)

func main() {
  var arr1 = [3]int{1,2,3}
  arr2 := [...]int{4,5,6,7,8}

  fmt.Println(arr1)
  fmt.Println(arr2)
  fmt.Println(5 ^ 6)

  for idx, val := range arr2 {
	fmt.Println("%v\t%v\n" , idx , val)
  }
}