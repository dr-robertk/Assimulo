      SUBROUTINE XERRWV (MSG, NMES, NERR, IERT, NI, I1, I2, NR, R1, R2)         
      INTEGER MSG, NMES, NERR, IERT, NI, I1, I2, NR,                            
     1   I, LUN, LUNIT, MESFLG, NWDS                                            
      DOUBLE PRECISION R1, R2                                                   
      DIMENSION MSG(NMES)                                                       
C-----------------------------------------------------------------------        
C SUBROUTINE XERRWV, AS GIVEN HERE, CONSTITUTES                                 
C A SIMPLIFIED VERSION OF THE SLATEC ERROR HANDLING PACKAGE.                    
C WRITTEN BY A. C. HINDMARSH AT LLL.  VERSION OF JANUARY 23, 1980.              
C MODIFIED BY L. R. PETZOLD, APRIL 1982.                                        
C THIS VERSION IS IN SINGLE PRECISION.                                          
C                                                                               
C ALL ARGUMENTS ARE INPUT ARGUMENTS.                                            
C                                                                               
C MSG    = THE MESSAGE (HOLLERITH LITTERAL OR INTEGER ARRAY).                   
C NMES   = THE LENGTH OF MSG (NUMBER OF CHARACTERS).                            
C NERR   = THE ERROR NUMBER (NOT USED).                                         
C IERT   = THE ERROR TYPE..                                                     
C          1 MEANS RECOVERABLE (CONTROL RETURNS TO CALLER).                     
C          2 MEANS FATAL (RUN IS ABORTED--SEE NOTE BELOW).                      
C NI     = NUMBER OF INTEGERS (0, 1, OR 2) TO BE PRINTED WITH MESSAGE.          
C I1,I2  = INTEGERS TO BE PRINTED, DEPENDING ON NI.                             
C NR     = NUMBER OF REALS (0, 1, OR 2) TO BE PRINTED WITH MESSAGE.             
C R1,R2  = REALS TO BE PRINTED, DEPENDING ON NI.                                
C                                                                               
C NOTE..  THIS ROUTINE IS MACHINE-DEPENDENT AND SPECIALIZED FOR USE             
C IN LIMITED CONTEXT, IN THE FOLLOWING WAYS..                                   
C 1. THE NUMBER OF HOLLERITH CHARACTERS STORED PER WORD, DENOTED                
C    BY NCPW BELOW, IS SET IN A DATA STATEMENT BELOW.                           
C 2. THE VALUE OF NMES IS ASSUMED TO BE AT MOST 60.                             
C    (MULTI-LINE MESSAGES ARE GENERATED BY REPEATED CALLS.)                     
C 3. IF IERT = 2, CONTROL PASSES TO THE STATEMENT   STOP                        
C    TO ABORT THE RUN.  THIS STATEMENT MAY BE MACHINE-DEPENDENT.                
C 4. R1 AND R2 ARE ASSUMED TO BE IN REAL AND ARE PRINTED                        
C    IN D21.13 FORMAT.                                                          
C 5. THE DATA STATEMENT BELOW CONTAINS DEFAULT VALUES OF                        
C       MESFLG = PRINT CONTROL FLAG..                                           
C                1 MEANS PRINT ALL MESSAGES (THE DEFAULT).                      
C                0 MEANS NO PRINTING.                                           
C       LUNIT  = LOGICAL UNIT NUMBER FOR MESSAGES.                              
C                THE DEFAULT IS 3 (MACHINE-DEPENDENT).                          
C                TO CHANGE LUNIT, CHANGE THE DATA STATEMENT                     
C                BELOW.                                                         
C-----------------------------------------------------------------------        
C THE FOLLOWING ARE INSTRUCTIONS FOR INSTALLING THIS ROUTINE                    
C IN DIFFERENT MACHINE ENVIRONMENTS.                                            
C                                                                               
C TO CHANGE THE DEFAULT OUTPUT UNIT, CHANGE THE DATA STATEMENT                  
C BELOW.                                                                        
C                                                                               
C FOR A DIFFERENT NUMBER OF CHARACTERS PER WORD, CHANGE THE                     
C DATA STATEMENT SETTING NCPW BELOW.                                            
C ALTERNATIVES FOR VARIOUS COMPUTERS ARE SHOWN IN COMMENT                       
C CARDS.                                                                        
C                                                                               
C FOR A DIFFERENT RUN-ABORT COMMAND, CHANGE THE STATEMENT FOLLOWING             
C STATEMENT 100 AT THE END.                                                     
C-----------------------------------------------------------------------        
C THE FOLLOWING VALUE OF NCPW IS VALID FOR THE CDC-6600 AND                     
C CDC-7600 COMPUTERS.                                                           
C     DATA NCPW/10/                                                             
C THE FOLLOWING IS VALID FOR THE CRAY-1 COMPUTER.                               
C     DATA NCPW/8/                                                              
C THE FOLLOWING IS VALID FOR THE BURROUGHS 6700 AND 7800 COMPUTERS.             
C     DATA NCPW/6/                                                              
C THE FOLLOWING IS VALID FOR THE PDP-10 COMPUTER.                               
C     DATA NCPW/5/                                                              
C THE FOLLOWING IS VALID FOR THE VAX COMPUTER WITH 4 BYTES PER INTEGER,         
C AND FOR THE IBM-360, IBM-303X, AND IBM-43XX COMPUTERS.                        
C     DATA NCPW/4/                                                              
C THE FOLLOWING IS VALID FOR THE PDP-11, OR VAX WITH 2-BYTE INTEGERS.           
C     DATA NCPW/2/                                                              
C----------------------------------------------------------------------         
      DIMENSION NFORM(13)                                                       
      DATA NFORM(1)/1H(/,NFORM(2)/1H1/,NFORM(3)/1HX/,NFORM(4)/1H,/,             
     1  NFORM(7)/1HA/,NFORM(10)/1H,/,NFORM(11)/1HA/,NFORM(13)/1H)/              
      DATA NCPW/4/                                                              
      DATA MESFLG/1/,LUNIT/6/                                                   
C                                                                               
      IF (MESFLG .EQ. 0) GO TO 100                                              
C GET LOGICAL UNIT NUMBER. ---------------------------------------------        
      LUN = LUNIT                                                               
C GET NUMBER OF WORDS IN MESSAGE. --------------------------------------        
      NCH = MIN0(NMES,60)                                                       
      NWDS = NCH/NCPW                                                           
      CALL S88FMT(2,NWDS,NFORM(5))                                              
      CALL S88FMT(2,NCPW,NFORM(8))                                              
      NREM = NCH - NWDS*NCPW                                                    
      IF (NREM .GT. 0) NWDS = NWDS + 1                                          
      IF (NREM .LT. 1) NREM = 1                                                 
      CALL S88FMT(1,NREM,NFORM(12))                                             
      WRITE(LUN,NFORM) (MSG(I),I=1,NWDS)                                        
      IF (NI .EQ. 1) WRITE (LUN, 20) I1                                         
 20   FORMAT(6X,23HIN ABOVE MESSAGE,  I1 =,I10)                                 
      IF (NI .EQ. 2) WRITE (LUN, 30) I1,I2                                      
 30   FORMAT(6X,23HIN ABOVE MESSAGE,  I1 =,I10,3X,4HI2 =,I10)                   
      IF (NR .EQ. 1) WRITE (LUN, 40) R1                                         
 40   FORMAT(6X,23HIN ABOVE MESSAGE,  R1 =,D21.13)                              
      IF (NR .EQ. 2) WRITE (LUN, 50) R1,R2                                      
 50   FORMAT(6X,15HIN ABOVE,  R1 =,D21.13,3X,4HR2 =,D21.13)                     
C ABORT THE RUN IF IERT = 2. -------------------------------------------        
 100  IF (IERT .NE. 2) RETURN                                                   
      STOP                                                                      
C----------------------- END OF SUBROUTINE XERRWV ----------------------        
      END                                                                       
      SUBROUTINE S88FMT(N,IVALUE,IFMT)                                          
C***BEGIN PROLOGUE  S88FMT                                                      
C***REFER TO  XERROR                                                            
C     ABSTRACT                                                                  
C        S88FMT REPLACES IFMT(1), ... ,IFMT(N) WITH THE                         
C        CHARACTERS CORRESPONDING TO THE N LEAST SIGNIFICANT                    
C        DIGITS OF IVALUE.                                                      
C                                                                               
C     TAKEN FROM THE BELL LABORATORIES PORT LIBRARY ERROR HANDLER               
C     LATEST REVISION ---  7 JUNE 1978                                          
C                                                                               
C***REFERENCES                                                                  
C   JONES R.E., *SLATEC COMMON MATHEMATICAL LIBRARY ERROR HANDLING              
C    PACKAGE*, SAND78-1189, SANDIA LABORATORIES, 1978.                          
C***ROUTINES CALLED  (NONE)                                                     
C***END PROLOGUE  S88FMT                                                        
C                                                                               
      DIMENSION IFMT(N),IDIGIT(10)                                              
      DATA IDIGIT(1),IDIGIT(2),IDIGIT(3),IDIGIT(4),IDIGIT(5),                   
     1     IDIGIT(6),IDIGIT(7),IDIGIT(8),IDIGIT(9),IDIGIT(10)                   
     2     /1H0,1H1,1H2,1H3,1H4,1H5,1H6,1H7,1H8,1H9/                            
C***FIRST EXECUTABLE STATEMENT  S88FMT                                          
      NT = N                                                                    
      IT = IVALUE                                                               
   10    IF (NT .EQ. 0) RETURN                                                  
         INDEX = MOD(IT,10)                                                     
         IFMT(NT) = IDIGIT(INDEX+1)                                             
         IT = IT/10                                                             
         NT = NT - 1                                                            
         GO TO 10                                                               
      END                                                                       
