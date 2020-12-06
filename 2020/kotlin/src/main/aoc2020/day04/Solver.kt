package main.aoc2020.day04

import java.io.File

fun main() {
    val fileContent = File("src/main/resources/day04input.txt").readText(Charsets.UTF_8)
        .split("\n\n")
    solve(fileContent)
    solve(fileContent, true)
}


fun solve(passportData: List<String>, doValidation: Boolean = false) {
    val passports: MutableSet<Passport> = mutableSetOf()
    passportData.map {
        try {
            passports.add(Passport(it.replace('\n', ' '), doValidation))
        } catch (e: Exception) {
            when (e) {
                is NumberFormatException, is IllegalStateException, is IllegalArgumentException -> {
//                    println("Accepted the exception: $e")
                }
                else -> throw e
            }
        }
    }
    println(passports.size)
}