import scala.annotation.tailrec

def f(arr: List[Int]): List[Int] = {
    @tailrec
    def doReverse(list: List[Int], acc: List[Int]): List[Int] = (list, acc) match {
        case (Nil, acc) => acc
        case (x :: xs, acc) => doReverse(xs, x :: acc)
    }
    
    doReverse(arr, Nil)
}
