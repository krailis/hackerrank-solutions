import java.io._
import java.math._
import java.security._
import java.text._
import java.util._
import java.util.concurrent._
import java.util.function._
import java.util.regex._
import java.util.stream._

import scala.annotation.tailrec

object Solution {

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val n = stdin.readLine.trim.toInt

        for (nItr <- 1 to n) {
            val x = stdin.readLine.trim.toDouble
            println((2 to 9).map(a => (Math.pow(x, a)/factorial(a)).toDouble).fold(1 + x)((b, a) => b + a))
        }
    }
    
    def factorial(n : Int): Int = {
        @tailrec
        def fact(x: Int, acc: Int): Int = (x, acc) match {
            case (0, acc) => acc
            case (x, acc) => fact(x-1, x * acc)
        }
        
        fact(n, 1)
    }
}

