import scala.annotation.tailrec
import scala.math.abs

def f(arr: List[Int]): Int = {
    @tailrec
    def sumOdd(list: List[Int], sum: Int): Int = (list, sum) match {
        case (Nil, sum) => sum
        case (x :: xs, sum) if abs(x) % 2 == 1 => sumOdd(xs, sum + x)
        case (x :: xs, sum) => sumOdd(xs, sum)
    }
    
    sumOdd(arr, 0)
}
