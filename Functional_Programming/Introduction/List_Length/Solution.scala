import scala.annotation.tailrec

def f(arr: List[Int]): Int = {
    @tailrec
    def length(list: List[Int], acc: Int): Int = (list, acc) match {
        case (Nil, acc) => acc
        case (x :: xs, acc) => length(xs, acc + 1)
    }
    
    length(arr, 0)
}
