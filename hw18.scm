;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname hw18) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Lenny Metlitsky
;IntroCS pd4 sec4
;Team name: The Rear End
;HW17 -- leap years and days in certian months
;2022-10-18
;time cost: 0.5 (hours)

; the isDivisibleBy function checks if b is a factor of a
(define isDivisibleBy
  (lambda (a b)
    (= (remainder a b) 0)
    ))

; the isCentury function checks if a year, y, is a century
(define isCentury
  (lambda (y)
    (isDivisibleBy y 100)
    ))

; (isLeapYr year) returns true if year is a leap year, false otherwise, according to these rules:
; Generally, a year divisible by 4 is a leap year.
; However, century years are not leap years unless they are divisible by 400.
; (e.g., 1700, 1800, and 1900 were not leap years, but 1600 and 2000 were.)
; the isLeapYr function checks if a year, y, is a leap year
(define isLeapYr
  (lambda (y)
    (and
     (isDivisibleBy y 4)
     (or
      (not (isCentury y))
      (and (isCentury y) (isDivisibleBy y 400))
      ))))

(isLeapYr 2000) "...should be true"
(isLeapYr 2004) "...should be true"
(isLeapYr 2008) "...should be true"
(isLeapYr 2009) "...should be false"
(isLeapYr 2100) "...should be false"
(isLeapYr 2104) "...should be true"
(isLeapYr 2200) "...should be false"
(isLeapYr 2300) "...should be false"
(isLeapYr 2400) "...should be true"


; the daysInMonth function takes numeric inputs (month year) and returns the number of days in the month specified.
; Assumes month is an integer from 1 to 12 and year is a 4-digit positive integer.
(define daysInMonth
  (lambda (m y)
    (if
     (= m 2)
     (if
      (isLeapYr y) 29 28
      )
     (if (< m 8)
         (
          if (isDivisibleBy m 2)
             30
             31
             )
         (
          if (isDivisibleBy m 2)
             31
             30
             )))))

(daysInMonth 1 2010) "...should be 31"
(daysInMonth 2 2011) "...should be 28"
(daysInMonth 2 2000) "...should be 29"
(daysInMonth 4 2011) "...should be 30"
(daysInMonth 10 2011) "...should be 31"
(daysInMonth 11 2011) "...should be 30"
(daysInMonth 10 2020) "...should be 31"
(daysInMonth 11 2020) "...should be 30"
