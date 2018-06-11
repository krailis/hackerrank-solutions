import scala.io.StdIn
import scala.math.abs

object Solution {
    
    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution*/
        val N = readInt()
        var initPoint = readLine().split(' ').map(_.toInt)
        var point = initPoint
        var area = 0.0
        for (_ <- 2 to N) {
            val nextPoint = readLine().split(' ').map(_.toInt)
            area += (point(0)*nextPoint(1) - point(1)*nextPoint(0))
            point = nextPoint
        }
        area += (point(0)*initPoint(1) - point(1)*initPoint(0))
        println(abs(area / 2))
    }
}
