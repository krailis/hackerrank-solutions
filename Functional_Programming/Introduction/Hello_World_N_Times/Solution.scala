object Solution extends App {

  object Solution {    
    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var n = sc.nextInt();
        //  Print "Hello World" on a new line 'n' times.
    }
  }

  //----------------------------------------------------

  def f(n: Int): Unit = {
    println("Hello World\n" * n)
  }

  //----------------------------------------------------

  var n = scala.io.StdIn.readInt
  f(n)
}

