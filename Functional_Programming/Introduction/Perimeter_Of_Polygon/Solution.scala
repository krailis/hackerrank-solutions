import scala.io.StdIn
import scala.math.{sqrt, pow}

object Solution {

    def main(args: Array[String]) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution*/
        val N = readInt()
        var initPoint = readLine().split(' ').map(_.toInt)
        var point = initPoint
        var perimeter = 0.0
        for (_ <- 2 to N) {
            val nextPoint = readLine().split(' ').map(_.toInt)
            perimeter += sqrt(pow(point(0) - nextPoint(0), 2) + pow(point(1) - nextPoint(1), 2))
            point = nextPoint
        }
        perimeter += sqrt(pow(point(0) - initPoint(0), 2) + pow(point(1) - initPoint(1), 2))
        println(perimeter)
    }
}
