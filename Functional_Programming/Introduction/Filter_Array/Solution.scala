import scala.annotation.tailrec

def f(delim:Int, arr:List[Int]): List[Int] = {
     
  @tailrec
  def filterArray(list: List[Int], acc: List[Int]): List[Int] = (list, acc) match {
    case (Nil, acc) => acc
    case (x :: xs, acc) if x < delim => filterArray(xs, acc ++ List(x))
    case (_ :: xs, acc) => filterArray(xs, acc)
  }
     
  filterArray(arr, Nil)
}

