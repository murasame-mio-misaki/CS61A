(define (merge ordered? s1 s2)
  ; BEGIN PROBLEM 16
  (cond ((null? s1) s2)
  ((null? s2) s1)
  (else 
    (if (ordered? (car s1) (car s2)) 
    (cons (car s1) (cons (car s2) (merge ordered? (cdr s1) (cdr s2)) ))
    (cons (car s2) (cons (car s1) (merge ordered? (cdr s1) (cdr s2)) ))
    )
  )
  )
  )