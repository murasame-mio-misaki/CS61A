(define-macro (repeat n expr)
  `(repeated-call ,n ,expr))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
      (f)
      (begin (f) (repeated-call (- n 1) f) )))
  

(repeated-call 2 (print 1))