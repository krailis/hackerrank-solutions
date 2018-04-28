import scala.annotation.tailrec

def f(arr:List[Int]): List[Int] = {
    
    @tailrec
    def filterPositions(list: List[Int], acc: List[Int]): List[Int] = (list, acc) match {
        case (Nil, acc) => acc
        case (_ :: Nil, acc) => acc
        case (_ :: y :: xs, acc) => filterPositions(xs, acc :+ y)
    }

    filterPositions(arr, Nil)
}

