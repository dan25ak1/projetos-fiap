SELECT INITCAP('JO�O DA SILVA') AS NOME
FROM DUAL;

SELECT LPAD(VL_SALARIO,10,'0') AS SALARIOS
FROM T_SIP_FUNCIONARIO;

SELECT ROUND(VL_SALARIO,2) VAL1, ROUND(VL_SALARIO,0) VAL2,ROUND(VL_SALARIO, -1) VAL3
FROM T_SIP_FUNCIONARIO;

SELECT ROUND(SYSDATE - TO_DATE('25/01/2006','DD/MM/YYYY'),0) DIAS_VIDA
FROM DUAL;

SELECT ROUND((SYSDATE - TO_DATE('25/01/2006','DD/MM/YYYY'))/ 365, 0)  DIAS_VIDA
FROM DUAL;

SELECT MAX(F.VL_SALARIO)
FROM T_SIP_FUNCIONARIO F
INNER JOIN T_SIP_DEPTO D ON (F.CD_DEPTO = D.CD_DEPTO);

SELECT D.CD_DEPTO, D.NM_DEPTO, SUM(F.VL_SALARIO)
FROM T_SIP_FUNCIONARIO F
INNER JOIN T_SIP_DEPTO D ON (F.CD_DEPTO = D.CD_DEPTO)
GROUP BY D.CD_DEPTO, D.NM_DEPTO
---HAVING AVG(F.VL_SALARIO) > 7000
ORDER BY 2;

SELECT F.CD_FUNC, F.NM_FUNCIONARIO, COUNT(D.ID_DEPENDENTE) AS QUANTIDADE_DEPENDENTES
FROM T_SIP_FUNCIONARIO F
INNER JOIN T_SIP_DEPENDENTE D ON F.CD_FUNC = D.CD_FUNC
GROUP BY F.CD_FUNC, F.NM_FUNCIONARIO
ORDER BY F.NM_FUNCIONARIO;