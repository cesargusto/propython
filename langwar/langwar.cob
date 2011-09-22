       IDENTIFICATION DIVISION.
       PROGRAM-ID.    LANGWAR.
       AUTHOR.        FABIANO WEIMAR DOS SANTOS.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
            SELECT ARQ
            ASSIGN       TO "ls.txt" 
            ORGANIZATION IS LINE SEQUENTIAL
            ACCESS MODE  IS SEQUENTIAL
            FILE STATUS  IS FS.

       DATA DIVISION.
       FILE SECTION.
       FD    ARQ
             LABEL RECORD IS STANDARD.
       01    REG-ARQ.
         03  FILLER                    PIC X(54).
         03  ARQUIVO1                  PIC X(20).
         03  ARQUIVO2 REDEFINES ARQUIVO1.
          05 LETRA                     PIC X(01) OCCURS 20 TIMES.

       WORKING-STORAGE SECTION.
       01    FS		               PIC 9(02).
       01    EXT-QTD.
        03   EXT                       PIC X(20) OCCURS 150 TIMES.
        03   QTD                       PIC 9(03) OCCURS 150 TIMES.
       01    BUFFER1                   PIC X(20).
       01    BUFFER2 REDEFINES BUFFER1.
        03   P1                        PIC X(01).
        03   P2-20                     PIC X(19).
       01    BUFFER3                   PIC X(20).
       77    POS-PONTO                 PIC 9(02).
       77    POS-FINAL                 PIC 9(02).
       77    QTDE-EXTENSOES            PIC 9(03).
       77    IND1                      PIC 9(03).
       77    IND2                      PIC 9(03).
       77    EXT-AUX                   PIC X(20).
       77    QTD-AUX                   PIC 9(03).

       PROCEDURE DIVISION.
       MAIN SECTION.
           OPEN INPUT ARQ.
           IF FS > 0
	     DISPLAY "Erro de Abertura: " FS
	     STOP RUN.
           MOVE  ZEROS                  TO  QTDE-EXTENSOES.
           PERFORM P100-INICIALIZA     THRU P199-FIM.
       LE-ARQUIVO.
	   READ ARQ AT END GO TO FIM. 
	   PERFORM P000-PROCESSA       THRU P099-FIM.
           GO TO LE-ARQUIVO.
       FIM.
	   PERFORM P300-ORDENA-LISTA   THRU P399-FIM.
	   PERFORM P400-LISTA          THRU P499-FIM.
	   CLOSE ARQ.
	   STOP RUN.

       P000-PROCESSA.
           MOVE  ZEROS                 TO  POS-PONTO POS-FINAL.
           MOVE  20                    TO  IND1.
       P010-PROCURA-FINAL.
           IF LETRA( IND1 ) NOT EQUAL SPACES
              MOVE  IND1               TO  POS-FINAL
              GO TO P020-PROCURA-PONTO.
           SUBTRACT 1                 FROM IND1.
           GO TO P010-PROCURA-FINAL.
       P020-PROCURA-PONTO.
           SUBTRACT 1                 FROM IND1.
           IF LETRA( IND1 ) EQUAL "."
              COMPUTE POS-PONTO = IND1 + 1
              GO TO P030-EXTENSAO.
           GO TO P020-PROCURA-PONTO.
       P030-EXTENSAO.
           MOVE  SPACES                TO  BUFFER1.
           MOVE  POS-FINAL             TO  IND1.
       P035-MONTA-EXTENSAO.
           MOVE  BUFFER1               TO  BUFFER3.
           MOVE  LETRA( IND1 )         TO  P1.
           MOVE  BUFFER3               TO  P2-20.
           SUBTRACT 1                 FROM IND1.
           IF IND1 < POS-PONTO
              GO TO P040-PROCESSA.
           GO TO P035-MONTA-EXTENSAO.
       P040-PROCESSA.           
           PERFORM P200-INCLUI-LISTA  THRU P299-FIM.
       P099-FIM.
           EXIT.

       P100-INICIALIZA.
           MOVE  ZEROS                 TO  IND1.
       P110-EXTENSAO.
           ADD   1                     TO  IND1.
           IF IND1 > 150
              GO TO P199-FIM.
           MOVE  SPACES                TO  EXT ( IND1 ).
           MOVE  ZEROS                 TO  QTD ( IND1 ).
           GO TO P110-EXTENSAO.
       P199-FIM.
           EXIT.

       P200-INCLUI-LISTA.
           MOVE  ZEROS                 TO  IND1.
       P210-LOOPING.
           ADD   1                     TO  IND1.
           IF IND1 > 150
              DISPLAY "Erro. Vetor Muito Pequeno."
              STOP RUN.
           IF IND1 > QTDE-EXTENSOES
              MOVE  IND1               TO  QTDE-EXTENSOES
              MOVE  BUFFER1            TO  EXT( IND1 )
              MOVE  1                  TO  QTD( IND1 )
              GO TO P299-FIM.
           IF EXT( IND1 ) = BUFFER1
              ADD   1                  TO  QTD( IND1 )
              GO TO P299-FIM.
           GO TO P210-LOOPING.
       P299-FIM.
           EXIT.

       P300-ORDENA-LISTA.
           MOVE  ZEROS                 TO  IND1.
       P310-LACO1.
           ADD   1                     TO  IND1. 
           IF IND1 > QTDE-EXTENSOES
              GO TO P399-FIM.
           MOVE  IND1                  TO  IND2.
       P320-LACO2.
           ADD   1                     TO  IND2.
           IF IND2 > QTDE-EXTENSOES
              GO TO P310-LACO1.
           IF QTD( IND2 ) > QTD( IND1 )
              MOVE  EXT( IND2 )        TO  EXT-AUX
              MOVE  QTD( IND2 )        TO  QTD-AUX
              MOVE  EXT( IND1 )        TO  EXT( IND2 )
              MOVE  QTD( IND1 )        TO  QTD( IND2 )
              MOVE  EXT-AUX            TO  EXT( IND1 )
              MOVE  QTD-AUX            TO  QTD( IND1 ).
           GO TO P320-LACO2.
       P399-FIM.
           EXIT.

       P400-LISTA.
           MOVE  ZEROS                 TO  IND1.
       P410-LOOPING.
           ADD   1                     TO  IND1.
           IF IND1 > QTDE-EXTENSOES
              GO TO P499-FIM.
           DISPLAY QTD( IND1 ) " " EXT( IND1 ).
           GO TO P410-LOOPING.
       P499-FIM.
           EXIT.
