import scala.annotation.tailrec

def f(num:Int, arr:List[Int]):List[Int] = {
    
    @tailrec
    def listReplication(n: Int, list: List[Int], acc: List[Int]): List[Int] = (n, list, acc) match {
        case (0, ls, _) => ls
        case (_, Nil, acc) => acc
        case (n, x :: xs, acc) => listReplication(n, xs, acc ++ List.fill(n)(x))
    }
    
    listReplication(num, arr, Nil)
}

