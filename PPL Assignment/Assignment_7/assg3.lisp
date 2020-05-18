
(defun fact1(n) ;;function for iterative method
    (setf f 1)
    (do ((i n (- i 1))) ((= i 1))
        (setf f (* f i))
    )
f)
(defvar n (read))
(format t "~&<<<Finding factorial of ~D>>>~&" n)
(format t "factorial = ~D (using iteration)" (fact1 n)))