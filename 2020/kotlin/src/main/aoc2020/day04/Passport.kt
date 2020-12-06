package main.aoc2020.day04

class Passport(passportData: String, doValidation: Boolean = false) {
    private val fieldValidations = mapOf(
        "byr" to ::validateByr, // (Birth Year)
        "iyr" to ::validateIyr, // (Issue Year)
        "eyr" to ::validateEyr, // (Expiration Year)
        "hgt" to ::validateHgt, // (Height)
        "hcl" to ::validateHcl, // (Hair Color)
        "ecl" to ::validateEcl, // (Eye Color)
        "pid" to ::validatePid  // (Passport ID)
    )

    init {
        val fields = passportData.split(" ")
            .associate {
                val (k, v) = it.split(":")
                k to v
            }.filterNot { it.key == "cid" }

        if (doValidation) {
            fieldValidations.keys.map {
                validateField(fields[it] ?: error("Field $it doesn't exist"), fieldValidations[it]!!)
            }
        } else {
            fieldValidations.keys.map {
                fields[it] ?: error("Field $it doesn't exist")
            }
        }
    }

    private fun validateField(field: String, validation_function: (String) -> Unit) {
        validation_function(field)
    }

    private fun validateByr(byr: String) {
        require(byr.toShort() in 1920..2002)
    }

    private fun validateIyr(iyr: String) {
        require(iyr.toShort() in 2010..2020)
    }

    private fun validateEyr(eyr: String) {
        require(eyr.toShort() in 2020..2030)
    }

    private fun validateHgt(hgt: String) {
        val heightFormat = hgt.substring(hgt.length - 2)
        val heightValue = hgt.substring(0, hgt.length - 2)
        with(heightFormat) {
            when {
                equals("cm") -> require(heightValue.toShort() in 150..193)
                equals("in") -> require(heightValue.toShort() in 59..76)
                else -> error("Invalid height metric")
            }
        }
    }

    private fun validateHcl(hcl: String) {
        require(hcl.matches("#[\\da-f]{6}".toRegex()))
    }

    private fun validateEcl(ecl: String) {
        require(ecl in arrayOf("amb", "blu", "brn", "gry", "grn", "hzl", "oth"))
    }

    private fun validatePid(pid: String) {
        require(pid.matches("\\d{9}".toRegex()))
    }
}