// Author:      Konstantinos Railis
// Github:      github.com/krailis
// Hackerrank:  hackerrank.com/krailis

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.lang.reflect.*;

class Singleton{

    private static final Singleton INSTANCE = new Singleton();

    private Singleton (){}

    public String str;

    static Singleton getSingleInstance() {
        return INSTANCE;
    }

}

