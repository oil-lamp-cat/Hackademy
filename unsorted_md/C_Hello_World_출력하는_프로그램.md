# C : Hello World 출력하는 프로그램

<aside>
💡 author : 전재호(agamtt) 2023-10-05

</aside>

이제 리눅스에서 내가 원하는 프로그램을 직접 코딩해서 만들어 볼 것 입니다.

여러가지 프로그래밍 언어 중 C언어를 먼저 써보겠습니다.

C언어로 코딩해서 프로그램을 만드는 과정은 아래와 같습니다.

1. C언어 파일을 만든다.
2. 그 파일을 텍스트에디터로 열어서 키보드로 C언어 코드를 입력한다.
    1. 텍스트에디터란, 메모장,vscode, vim, nano 등을 말합니다.
3. C언어 컴파일러를 이용하여 컴파일한다.
    1. 컴파일은 코딩한 것을 프로그램으로 변환하는 것을 의미합니다.
    2. 컴파일러는 컴파일을 해주는 프로그램입니다. (설치해야함)
4. 만들어진 프로그램을 실행해서 쓴다.

### 1. C언어 파일 만들기

멋진 텍스트에디터인 nano를 이용하여 C언어 파일을 만듭니다.

일단 nano 가 설치되어있는지 확인합니다

![Untitled](Untitled%2095.png)

nano 를 설치합니다. (설치가 된 경우, 넘어가세요)

```bash
apt update
apt install nano
```

다음을 입력하여 c언어파일을 생성합니다.

c언어파일은 .c 로 끝납니다. (이렇게 .뒤에 붙어서 그 파일이 어떤 파일인지 알려주는 것을 확장자라고 부릅니다.)

참고로 반드시 유저의 홈폴더에서 해야합니다. (다른 디렉토리에는 쓰기권한이 없으니까요)

```bash
cd ~
```

파일이름은 hello 나 아무거나 해도 됩니다. 확장자는 c언어 코드파일인 .c 로 해야합니다.

```bash
nano hello.c
```

![Untitled](Untitled%2099.png)

그러면 이렇게 편집기가 열립니다.

![Untitled](Untitled%2096.png)

이렇게 입력합니다.

```c
#include <stdio.h>

int main(){
	puts("hello world!");
}
```

세미콜론(;) 이 없으면 c언어는 줄이 넘어가는 것을 구분하지 못합니다. 꼭 붙여야 합니다.

이제 Ctrl + x 를 누르고, Save Modified Buffer? 가 뜨면 Y 를 누르고, 엔터를 치면 파일이 저장됩니다.

![Untitled](Untitled%20100.png)

### gcc

이제 gcc 를 이용하여 c 코드파일을 컴파일해서 실행해보겠습니다.

![Untitled](Untitled%20101.png)

그러면 a.out 이라는 파일이 생깁니다. out 은 실행가능한 파일의 확장자입니다. 이 파일은 실행가능한 파일입니다.

이제 이 파일을 실행해봅니다.

그냥 a.out 이라고 입력하면 리눅스는 /bin 에서 찾습니다. 당연히 없습니다 우리가 방금 만든 파일이니까요. 반드시 경로를 명시해서 실행해야 리눅스가 위치를 찾을 수 있습니다.

```bash
/home/superhacker/a.out
```

그러나 이렇게 입력하면 기니까, 전에 배웠던 dot 를 쓰면 편합니다. dot(점) 한개는 현재 경로를 의미하니, dot 과 slash 를 붙이면 현재 디렉토리에 있는 a.out 이 실행됩니다.

```bash
./a.out
```

![Untitled](Untitled%20102.png)

그러면 아까 입력했던 hello world! 가 출력됩니다.

만일, 실행파일의 이름을 지정하고 싶으면 gcc 의 output 옵션에 입력하면됩니다.

```bash
gcc -o myProgram hello.c
```

![Untitled](Untitled%20103.png)

마찬가지로 실행됩니다.

### 놀라운 사실 : 명령어는 사실 프로그램이였다

전에 리눅스의 명령어는 모두 /bin 에 저장되어있다고 했습니다.

그러면 우리가 만든 프로그램을 /bin 으로 옮기면 어떻게 될까요?

```bash
mv myProgram /bin
myProgram
```

![Untitled](Untitled%20104.png)

놀랍게도 경로를 명시하지 않아도 실행됩니다.

리눅스는 경로를 명시하지 않으면 /bin 에서 찾아본다고 했습니다.

즉, 명령어 = 컴파일된 프로그램 이고, 컴파일된 프로그램이 /bin 에 있으면 그 명령어를 실행할 수 있게 됩니다.

이제 리눅스 명령어를 내맘대로 만들수있게 되었다는겁니다 

### 작동원리

우리 조상님들은 일찍이 C라는 것을 이용해서 프로그램을 만들었습니다.

C언어의 작동원리는 python보다 복잡합니다.

컴퓨터공학과나 전자공학과를 가면 “진짜로” 어떻게 동작하는지 배웁니다만 그건 2년씩 걸립니다.

따라서 간단하게 어떻게 작동하는지 설명하겠습니다.

우선 프로그램은 “함수”라는 구조로 작동합니다.

고등학교 때 배운 함수라는 건 이렇게 생겼습니다.

$$
y=f(x)
$$

x 에 숫자를 넣으면, f 에서 뭔 일이 일어난다음 y 에 그 결과가 대입됩니다.

함수에 함수를 넣을 수 있다는 것도 알 것입니다.

$$
y = f(g(x))
$$

옛날 컴퓨터를 만든 놈들은 수학자들이였기 때문에, 컴퓨터는 이런 방식으로 작동합니다.

```bash
int hello(int a){
	이 안에 함수의 실제 식이 들어감
	return 함수 계산이 끝났을 때 밖으로 나가서 y 에 저장되는 숫자
}
```

이것은 함수를 만드는 코드입니다.

int 는 integer의 약자인데, 이진수를 8개 저장할 수 있는 크기를 의미합니다.

만약 f(x) 를 계산한 결과가 범위를 초과하면 오류가 발생합니다.

범위를 쓰는 이유는 범위로 가능한 값을 적게 쓰면 컴퓨터를 아껴 쓸수있기 때문입니다.

<aside>
🔥 python 은 이 범위를 지가 알아서 예측합니다. c언어는 조상님들이 만든 언어여서 그땐 그런 기능이 없었습니다.k

</aside>

```bash
함수이름 f : hello
함수의 결과의 범위 : int
함수에 집어넣는 x : 범위가 int 고 이름이 a
```

return 을 누가 한국어로 번역했는지는 모르지만, “반환”이라고 번역을 했습니다.

return 뒤에 나오는 숫자를 “반환값” 또는 “return value” 라고 부릅니다.

컴퓨터에서 실행되는 모든 프로그램 나부랭이는 함수안에 함수를 집어넣고 함수안에 함수를 집어넣고… 하면서 실행됩니다.

예를 들어, hello 하고 화면에 인사를 출력하는 함수는 이렇게 작동합니다.

```bash
int hello(){
	print("hello~~");
	return 0;
}
```

$$
y = hello(print(x))
$$

뭐 이런거임. print 는 또 뭔가 안에 적혀있겠지

우선, 리눅스는 프로그램을 실행시키면,

main 이라는 이름의 함수를 찾아서 실행시킵니다.

그래서 main 이 반드시 있어야합니다.

main 안에 식을 넣으면, 컴퓨터가 그 식을 실행합니다.

그리고 return value 가 0 이면 정상적으로 작동했다고 생각하고 프로그램을 끕니다.

이런 프로그램을 만들어봅시다.

```bash
nano hello.c
코드 입력
int main(){
	1+2;
}
Ctrl + X 치고 Y 치고 Enter
gcc hello.c
./a.out
```

![Untitled](Untitled%20105.png)

![Untitled](Untitled%20106.png)

그러면 놀랍게도 아무일도 일어나지 않습니다.

사실 1+2 가 컴퓨터 안에서 계산되었습니다.

그리고 프로그램이 꺼진거죠

하지만 컴퓨터는 우리가 시킨 일만 하기 때문에 “화면에 보여주기” 를 안한겁니다.

1 과 2를 더한다음 화면에 보여주기를 원한다면, 화면에 보여주는 코드를 적어넣어야 합니다.

### 화면에 보여주기 코드

화면에 뭔가 보여주는 코드는 **거의 무조건 직접 코드를 짜지 않고 남이 만든 함수를 사용합니다.**

곰곰히 생각해보면 화면에 뭔가를 보여주는 코드가 몹시 복잡할 것임을 알 수 있습니다.

1. 화면 어디에 어떤 글자를 어떤 크기로 보여줄지 정해야함
2. 무슨 색깔로 보여줄지 정해야함
3. 등등…

이 코드는 실제로 이렇게 생겼습니다.

- 클릭해서 보기/접기
    
    ```c
    #include <array_length.h>
    #include <ctype.h>
    #include <limits.h>
    #include <printf.h>
    #include <stdarg.h>
    #include <stdint.h>
    #include <stdlib.h>
    #include <string.h>
    #include <errno.h>
    #include <wchar.h>
    #include <libc-lock.h>
    #include <sys/param.h>
    #include <_itoa.h>
    #include <locale/localeinfo.h>
    #include <stdio.h>
    #include <scratch_buffer.h>
    #include <intprops.h>
    /* This code is shared between the standard stdio implementation found
       in GNU C library and the libio implementation originally found in
       GNU libg++.
       Beside this it is also shared between the normal and wide character
       implementation as defined in ISO/IEC 9899:1990/Amendment 1:1995.  */
    #include <libioP.h>
    #ifdef COMPILE_WPRINTF
    #include <wctype.h>
    #endif
    #define ARGCHECK(S, Format) \
      do									      \
        {									      \
          /* Check file argument for consistence.  */			      \
          CHECK_FILE (S, -1);						      \
          if (S->_flags & _IO_NO_WRITES)					      \
    	{								      \
    	  S->_flags |= _IO_ERR_SEEN;					      \
    	  __set_errno (EBADF);						      \
    	  return -1;							      \
    	}								      \
          if (Format == NULL)						      \
    	{								      \
    	  __set_errno (EINVAL);						      \
    	  return -1;							      \
    	}								      \
        } while (0)
    #define UNBUFFERED_P(S) ((S)->_flags & _IO_UNBUFFERED)
    #if __HAVE_FLOAT128_UNLIKE_LDBL
    # define PARSE_FLOAT_VA_ARG_EXTENDED(INFO)				      \
      do									      \
        {									      \
          if (is_long_double						      \
    	  && (mode_flags & PRINTF_LDBL_USES_FLOAT128) != 0)		      \
    	{								      \
    	  INFO.is_binary128 = 1;					      \
    	  the_arg.pa_float128 = va_arg (ap, _Float128);			      \
    	}								      \
          else								      \
    	{								      \
    	  PARSE_FLOAT_VA_ARG (INFO);					      \
    	}								      \
        }									      \
      while (0)
    #else
    # define PARSE_FLOAT_VA_ARG_EXTENDED(INFO)				      \
      PARSE_FLOAT_VA_ARG (INFO);
    #endif
    #define PARSE_FLOAT_VA_ARG(INFO)					      \
      do									      \
        {									      \
          INFO.is_binary128 = 0;						      \
          if (is_long_double)						      \
    	the_arg.pa_long_double = va_arg (ap, long double);		      \
          else								      \
    	the_arg.pa_double = va_arg (ap, double);			      \
        }									      \
      while (0)
    #if __HAVE_FLOAT128_UNLIKE_LDBL
    # define SETUP_FLOAT128_INFO(INFO)					      \
      do									      \
        {									      \
          if ((mode_flags & PRINTF_LDBL_USES_FLOAT128) != 0)		      \
    	INFO.is_binary128 = is_long_double;				      \
          else								      \
    	INFO.is_binary128 = 0;						      \
        }									      \
      while (0)
    #else
    # define SETUP_FLOAT128_INFO(INFO)					      \
      do									      \
        {									      \
          INFO.is_binary128 = 0;						      \
        }									      \
      while (0)
    #endif
    /* Add LENGTH to DONE.  Return the new value of DONE, or -1 on
       overflow (and set errno accordingly).  */
    static inline int
    done_add_func (size_t length, int done)
    {
      if (done < 0)
        return done;
      int ret;
      if (INT_ADD_WRAPV (done, length, &ret))
        {
          __set_errno (EOVERFLOW);
          return -1;
        }
      return ret;
    }
    #define done_add(val)							\
      do									\
        {									\
          /* Ensure that VAL has a type similar to int.  */			\
          _Static_assert (sizeof (val) == sizeof (int), "value int size");	\
          _Static_assert ((__typeof__ (val)) -1 < 0, "value signed");	\
          done = done_add_func ((val), done);				\
          if (done < 0)							\
    	goto all_done;							\
        }									\
      while (0)
    #ifndef COMPILE_WPRINTF
    # define vfprintf	__vfprintf_internal
    # define CHAR_T		char
    # define OTHER_CHAR_T   wchar_t
    # define UCHAR_T	unsigned char
    # define INT_T		int
    typedef const char *THOUSANDS_SEP_T;
    # define L_(Str)	Str
    # define ISDIGIT(Ch)	((unsigned int) ((Ch) - '0') < 10)
    # define STR_LEN(Str)	strlen (Str)
    # define PUT(F, S, N)	_IO_sputn ((F), (S), (N))
    # define PUTC(C, F)	_IO_putc_unlocked (C, F)
    # define ORIENT		if (_IO_vtable_offset (s) == 0 && _IO_fwide (s, -1) != -1)\
    			  return -1
    # define CONVERT_FROM_OTHER_STRING __wcsrtombs
    #else
    # define vfprintf	__vfwprintf_internal
    # define CHAR_T		wchar_t
    # define OTHER_CHAR_T   char
    /* This is a hack!!!  There should be a type uwchar_t.  */
    # define UCHAR_T	unsigned int /* uwchar_t */
    # define INT_T		wint_t
    typedef wchar_t THOUSANDS_SEP_T;
    # define L_(Str)	L##Str
    # define ISDIGIT(Ch)	((unsigned int) ((Ch) - L'0') < 10)
    # define STR_LEN(Str)	__wcslen (Str)
    # include <_itowa.h>
    # define PUT(F, S, N)	_IO_sputn ((F), (S), (N))
    # define PUTC(C, F)	_IO_putwc_unlocked (C, F)
    # define ORIENT		if (_IO_fwide (s, 1) != 1) return -1
    # define CONVERT_FROM_OTHER_STRING __mbsrtowcs
    # undef _itoa
    # define _itoa(Val, Buf, Base, Case) _itowa (Val, Buf, Base, Case)
    # define _itoa_word(Val, Buf, Base, Case) _itowa_word (Val, Buf, Base, Case)
    # undef EOF
    # define EOF WEOF
    #endif
    static inline int
    pad_func (FILE *s, CHAR_T padchar, int width, int done)
    {
      if (width > 0)
        {
          ssize_t written;
    #ifndef COMPILE_WPRINTF
          written = _IO_padn (s, padchar, width);
    #else
          written = _IO_wpadn (s, padchar, width);
    #endif
          if (__glibc_unlikely (written != width))
    	return -1;
          return done_add_func (width, done);
        }
      return done;
    }
    #define PAD(Padchar)							\
      do									\
        {									\
          done = pad_func (s, (Padchar), width, done);			\
          if (done < 0)							\
    	goto all_done;							\
        }									\
      while (0)
    #include "_i18n_number.h"
    /* Include the shared code for parsing the format string.  */
    #include "printf-parse.h"
    #define	outchar(Ch)							      \
      do									      \
        {									      \
          const INT_T outc = (Ch);						      \
          if (PUTC (outc, s) == EOF || done == INT_MAX)			      \
    	{								      \
    	  done = -1;							      \
    	  goto all_done;						      \
    	}								      \
          ++done;								      \
        }									      \
      while (0)
    static inline int
    outstring_func (FILE *s, const UCHAR_T *string, size_t length, int done)
    {
      assert ((size_t) done <= (size_t) INT_MAX);
      if ((size_t) PUT (s, string, length) != (size_t) (length))
        return -1;
      return done_add_func (length, done);
    }
    #define outstring(String, Len)						\
      do									\
        {									\
          const void *string_ = (String);					\
          done = outstring_func (s, string_, (Len), done);			\
          if (done < 0)							\
    	goto all_done;							\
        }									\
       while (0)
    /* Write the string SRC to S.  If PREC is non-negative, write at most
       PREC bytes.  If LEFT is true, perform left justification.  */
    static int
    outstring_converted_wide_string (FILE *s, const OTHER_CHAR_T *src, int prec,
    				 int width, bool left, int done)
    {
      /* Use a small buffer to combine processing of multiple characters.
         CONVERT_FROM_OTHER_STRING expects the buffer size in (wide)
         characters, and buf_length counts that.  */
      enum { buf_length = 256 / sizeof (CHAR_T) };
      CHAR_T buf[buf_length];
      _Static_assert (sizeof (buf) > MB_LEN_MAX,
    		  "buffer is large enough for a single multi-byte character");
      /* Add the initial padding if needed.  */
      if (width > 0 && !left)
        {
          /* Make a first pass to find the output width, so that we can
    	 add the required padding.  */
          mbstate_t mbstate = { 0 };
          const OTHER_CHAR_T *src_copy = src;
          size_t total_written;
          if (prec < 0)
    	total_written = CONVERT_FROM_OTHER_STRING
    	  (NULL, &src_copy, 0, &mbstate);
          else
    	{
    	  /* The source might not be null-terminated.  Enforce the
    	     limit manually, based on the output length.  */
    	  total_written = 0;
    	  size_t limit = prec;
    	  while (limit > 0 && src_copy != NULL)
    	    {
    	      size_t write_limit = buf_length;
    	      if (write_limit > limit)
    		write_limit = limit;
    	      size_t written = CONVERT_FROM_OTHER_STRING
    		(buf, &src_copy, write_limit, &mbstate);
    	      if (written == (size_t) -1)
    		return -1;
    	      if (written == 0)
    		break;
    	      total_written += written;
    	      limit -= written;
    	    }
    	}
          /* Output initial padding.  */
          if (total_written < width)
    	{
    	  done = pad_func (s, L_(' '), width - total_written, done);
    	  if (done < 0)
    	    return done;
    	}
        }
      /* Convert the input string, piece by piece.  */
      size_t total_written = 0;
      {
        mbstate_t mbstate = { 0 };
        /* If prec is negative, remaining is not decremented, otherwise,
          it serves as the write limit.  */
        size_t remaining = -1;
        if (prec >= 0)
          remaining = prec;
        while (remaining > 0 && src != NULL)
          {
    	size_t write_limit = buf_length;
    	if (remaining < write_limit)
    	  write_limit = remaining;
    	size_t written = CONVERT_FROM_OTHER_STRING
    	  (buf, &src, write_limit, &mbstate);
    	if (written == (size_t) -1)
    	  return -1;
    	if (written == 0)
    	  break;
    	done = outstring_func (s, (const UCHAR_T *) buf, written, done);
    	if (done < 0)
    	  return done;
    	total_written += written;
    	if (prec >= 0)
    	  remaining -= written;
          }
      }
      /* Add final padding.  */
      if (width > 0 && left && total_written < width)
        return pad_func (s, L_(' '), width - total_written, done);
      return done;
    }
    /* Calls __printf_fp or __printf_fphex based on the value of the
       format specifier INFO->spec.  */
    static inline int
    __printf_fp_spec (FILE *fp, const struct printf_info *info,
    		  const void *const *args)
    {
      if (info->spec == 'a' || info->spec == 'A')
        return __printf_fphex (fp, info, args);
      else
        return __printf_fp (fp, info, args);
    }
    /* For handling long_double and longlong we use the same flag.  If
       `long' and `long long' are effectively the same type define it to
       zero.  */
    #if LONG_MAX == LONG_LONG_MAX
    # define is_longlong 0
    #else
    # define is_longlong is_long_double
    #endif
    /* If `long' and `int' is effectively the same type we don't have to
       handle `long separately.  */
    #if INT_MAX == LONG_MAX
    # define is_long_num	0
    #else
    # define is_long_num	is_long
    #endif
    /* Global constants.  */
    static const CHAR_T null[] = L_("(null)");
    /* Size of the work_buffer variable (in characters, not bytes.  */
    enum { WORK_BUFFER_SIZE = 1000 / sizeof (CHAR_T) };
    /* This table maps a character into a number representing a class.  In
       each step there is a destination label for each class.  */
    static const uint8_t jump_table[] =
      {
        /* ' ' */  1,            0,            0, /* '#' */  4,
    	       0, /* '%' */ 14,            0, /* '\''*/  6,
    	       0,            0, /* '*' */  7, /* '+' */  2,
    	       0, /* '-' */  3, /* '.' */  9,            0,
        /* '0' */  5, /* '1' */  8, /* '2' */  8, /* '3' */  8,
        /* '4' */  8, /* '5' */  8, /* '6' */  8, /* '7' */  8,
        /* '8' */  8, /* '9' */  8,            0,            0,
    	       0,            0,            0,            0,
    	       0, /* 'A' */ 26, /* 'B' */ 30, /* 'C' */ 25,
    	       0, /* 'E' */ 19, /* F */   19, /* 'G' */ 19,
    	       0, /* 'I' */ 29,            0,            0,
        /* 'L' */ 12,            0,            0,            0,
    	       0,            0,            0, /* 'S' */ 21,
    	       0,            0,            0,            0,
        /* 'X' */ 18,            0, /* 'Z' */ 13,            0,
    	       0,            0,            0,            0,
    	       0, /* 'a' */ 26, /* 'b' */ 30, /* 'c' */ 20,
        /* 'd' */ 15, /* 'e' */ 19, /* 'f' */ 19, /* 'g' */ 19,
        /* 'h' */ 10, /* 'i' */ 15, /* 'j' */ 28,            0,
        /* 'l' */ 11, /* 'm' */ 24, /* 'n' */ 23, /* 'o' */ 17,
        /* 'p' */ 22, /* 'q' */ 12,            0, /* 's' */ 21,
        /* 't' */ 27, /* 'u' */ 16,            0,            0,
        /* 'x' */ 18,            0, /* 'z' */ 13
      };
    #define NOT_IN_JUMP_RANGE(Ch) ((Ch) < L_(' ') || (Ch) > L_('z'))
    #define CHAR_CLASS(Ch) (jump_table[(INT_T) (Ch) - L_(' ')])
    #define LABEL(Name) do_##Name
    #ifdef SHARED
      /* 'int' is enough and it saves some space on 64 bit systems.  */
    # define JUMP_TABLE_TYPE const int
    # define JUMP_TABLE_BASE_LABEL do_form_unknown
    # define REF(Name) &&do_##Name - &&JUMP_TABLE_BASE_LABEL
    # define JUMP(ChExpr, table)						      \
          do								      \
    	{								      \
    	  int offset;							      \
    	  void *ptr;							      \
    	  spec = (ChExpr);						      \
    	  offset = NOT_IN_JUMP_RANGE (spec) ? REF (form_unknown)	      \
    	    : table[CHAR_CLASS (spec)];					      \
    	  ptr = &&JUMP_TABLE_BASE_LABEL + offset;			      \
    	  goto *ptr;							      \
    	}								      \
          while (0)
    #else
    # define JUMP_TABLE_TYPE const void *const
    # define REF(Name) &&do_##Name
    # define JUMP(ChExpr, table)						      \
          do								      \
    	{								      \
    	  const void *ptr;						      \
    	  spec = (ChExpr);						      \
    	  ptr = NOT_IN_JUMP_RANGE (spec) ? REF (form_unknown)		      \
    	    : table[CHAR_CLASS (spec)];					      \
    	  goto *ptr;							      \
    	}								      \
          while (0)
    #endif
    #define STEP0_3_TABLE							      \
        /* Step 0: at the beginning.  */					      \
        static JUMP_TABLE_TYPE step0_jumps[31] =				      \
        {									      \
          REF (form_unknown),						      \
          REF (flag_space),		/* for ' ' */				      \
          REF (flag_plus),		/* for '+' */				      \
          REF (flag_minus),		/* for '-' */				      \
          REF (flag_hash),		/* for '<hash>' */			      \
          REF (flag_zero),		/* for '0' */				      \
          REF (flag_quote),		/* for '\'' */				      \
          REF (width_asterics),	/* for '*' */				      \
          REF (width),		/* for '1'...'9' */			      \
          REF (precision),		/* for '.' */				      \
          REF (mod_half),		/* for 'h' */				      \
          REF (mod_long),		/* for 'l' */				      \
          REF (mod_longlong),	/* for 'L', 'q' */			      \
          REF (mod_size_t),		/* for 'z', 'Z' */			      \
          REF (form_percent),	/* for '%' */				      \
          REF (form_integer),	/* for 'd', 'i' */			      \
          REF (form_unsigned),	/* for 'u' */				      \
          REF (form_octal),		/* for 'o' */				      \
          REF (form_hexa),		/* for 'X', 'x' */			      \
          REF (form_float),		/* for 'E', 'e', 'F', 'f', 'G', 'g' */	      \
          REF (form_character),	/* for 'c' */				      \
          REF (form_string),	/* for 's', 'S' */			      \
          REF (form_pointer),	/* for 'p' */				      \
          REF (form_number),	/* for 'n' */				      \
          REF (form_strerror),	/* for 'm' */				      \
          REF (form_wcharacter),	/* for 'C' */				      \
          REF (form_floathex),	/* for 'A', 'a' */			      \
          REF (mod_ptrdiff_t),      /* for 't' */				      \
          REF (mod_intmax_t),       /* for 'j' */				      \
          REF (flag_i18n),		/* for 'I' */				      \
          REF (form_binary),	/* for 'B', 'b' */			      \
        };									      \
        /* Step 1: after processing width.  */				      \
        static JUMP_TABLE_TYPE step1_jumps[31] =				      \
        {									      \
          REF (form_unknown),						      \
          REF (form_unknown),	/* for ' ' */				      \
          REF (form_unknown),	/* for '+' */				      \
          REF (form_unknown),	/* for '-' */				      \
          REF (form_unknown),	/* for '<hash>' */			      \
          REF (form_unknown),	/* for '0' */				      \
          REF (form_unknown),	/* for '\'' */				      \
          REF (form_unknown),	/* for '*' */				      \
          REF (form_unknown),	/* for '1'...'9' */			      \
          REF (precision),		/* for '.' */				      \
          REF (mod_half),		/* for 'h' */				      \
          REF (mod_long),		/* for 'l' */				      \
          REF (mod_longlong),	/* for 'L', 'q' */			      \
          REF (mod_size_t),		/* for 'z', 'Z' */			      \
          REF (form_percent),	/* for '%' */				      \
          REF (form_integer),	/* for 'd', 'i' */			      \
          REF (form_unsigned),	/* for 'u' */				      \
          REF (form_octal),		/* for 'o' */				      \
          REF (form_hexa),		/* for 'X', 'x' */			      \
          REF (form_float),		/* for 'E', 'e', 'F', 'f', 'G', 'g' */	      \
          REF (form_character),	/* for 'c' */				      \
          REF (form_string),	/* for 's', 'S' */			      \
          REF (form_pointer),	/* for 'p' */				      \
          REF (form_number),	/* for 'n' */				      \
          REF (form_strerror),	/* for 'm' */				      \
          REF (form_wcharacter),	/* for 'C' */				      \
          REF (form_floathex),	/* for 'A', 'a' */			      \
          REF (mod_ptrdiff_t),      /* for 't' */				      \
          REF (mod_intmax_t),       /* for 'j' */				      \
          REF (form_unknown),       /* for 'I' */				      \
          REF (form_binary),	/* for 'B', 'b' */			      \
        };									      \
        /* Step 2: after processing precision.  */				      \
        static JUMP_TABLE_TYPE step2_jumps[31] =				      \
        {									      \
          REF (form_unknown),						      \
          REF (form_unknown),	/* for ' ' */				      \
          REF (form_unknown),	/* for '+' */				      \
          REF (form_unknown),	/* for '-' */				      \
          REF (form_unknown),	/* for '<hash>' */			      \
          REF (form_unknown),	/* for '0' */				      \
          REF (form_unknown),	/* for '\'' */				      \
          REF (form_unknown),	/* for '*' */				      \
          REF (form_unknown),	/* for '1'...'9' */			      \
          REF (form_unknown),	/* for '.' */				      \
          REF (mod_half),		/* for 'h' */				      \
          REF (mod_long),		/* for 'l' */				      \
          REF (mod_longlong),	/* for 'L', 'q' */			      \
          REF (mod_size_t),		/* for 'z', 'Z' */			      \
          REF (form_percent),	/* for '%' */				      \
          REF (form_integer),	/* for 'd', 'i' */			      \
          REF (form_unsigned),	/* for 'u' */				      \
          REF (form_octal),		/* for 'o' */				      \
          REF (form_hexa),		/* for 'X', 'x' */			      \
          REF (form_float),		/* for 'E', 'e', 'F', 'f', 'G', 'g' */	      \
          REF (form_character),	/* for 'c' */				      \
          REF (form_string),	/* for 's', 'S' */			      \
          REF (form_pointer),	/* for 'p' */				      \
          REF (form_number),	/* for 'n' */				      \
          REF (form_strerror),	/* for 'm' */				      \
          REF (form_wcharacter),	/* for 'C' */				      \
          REF (form_floathex),	/* for 'A', 'a' */			      \
          REF (mod_ptrdiff_t),      /* for 't' */				      \
          REF (mod_intmax_t),       /* for 'j' */				      \
          REF (form_unknown),       /* for 'I' */				      \
          REF (form_binary),	/* for 'B', 'b' */			      \
        };									      \
        /* Step 3a: after processing first 'h' modifier.  */		      \
        static JUMP_TABLE_TYPE step3a_jumps[31] =				      \
        {									      \
          REF (form_unknown),						      \
          REF (form_unknown),	/* for ' ' */				      \
          REF (form_unknown),	/* for '+' */				      \
          REF (form_unknown),	/* for '-' */				      \
          REF (form_unknown),	/* for '<hash>' */			      \
          REF (form_unknown),	/* for '0' */				      \
          REF (form_unknown),	/* for '\'' */				      \
          REF (form_unknown),	/* for '*' */				      \
          REF (form_unknown),	/* for '1'...'9' */			      \
          REF (form_unknown),	/* for '.' */				      \
          REF (mod_halfhalf),	/* for 'h' */				      \
          REF (form_unknown),	/* for 'l' */				      \
          REF (form_unknown),	/* for 'L', 'q' */			      \
          REF (form_unknown),	/* for 'z', 'Z' */			      \
          REF (form_percent),	/* for '%' */				      \
          REF (form_integer),	/* for 'd', 'i' */			      \
          REF (form_unsigned),	/* for 'u' */				      \
          REF (form_octal),		/* for 'o' */				      \
          REF (form_hexa),		/* for 'X', 'x' */			      \
          REF (form_unknown),	/* for 'E', 'e', 'F', 'f', 'G', 'g' */	      \
          REF (form_unknown),	/* for 'c' */				      \
          REF (form_unknown),	/* for 's', 'S' */			      \
          REF (form_unknown),	/* for 'p' */				      \
          REF (form_number),	/* for 'n' */				      \
          REF (form_unknown),	/* for 'm' */				      \
          REF (form_unknown),	/* for 'C' */				      \
          REF (form_unknown),	/* for 'A', 'a' */			      \
          REF (form_unknown),       /* for 't' */				      \
          REF (form_unknown),       /* for 'j' */				      \
          REF (form_unknown),       /* for 'I' */				      \
          REF (form_binary),	/* for 'B', 'b' */			      \
        };									      \
        /* Step 3b: after processing first 'l' modifier.  */		      \
        static JUMP_TABLE_TYPE step3b_jumps[31] =				      \
        {									      \
          REF (form_unknown),						      \
          REF (form_unknown),	/* for ' ' */				      \
          REF (form_unknown),	/* for '+' */				      \
          REF (form_unknown),	/* for '-' */				      \
          REF (form_unknown),	/* for '<hash>' */			      \
          REF (form_unknown),	/* for '0' */				      \
          REF (form_unknown),	/* for '\'' */				      \
          REF (form_unknown),	/* for '*' */				      \
          REF (form_unknown),	/* for '1'...'9' */			      \
          REF (form_unknown),	/* for '.' */				      \
          REF (form_unknown),	/* for 'h' */				      \
          REF (mod_longlong),	/* for 'l' */				      \
          REF (form_unknown),	/* for 'L', 'q' */			      \
          REF (form_unknown),	/* for 'z', 'Z' */			      \
          REF (form_percent),	/* for '%' */				      \
          REF (form_integer),	/* for 'd', 'i' */			      \
          REF (form_unsigned),	/* for 'u' */				      \
          REF (form_octal),		/* for 'o' */				      \
          REF (form_hexa),		/* for 'X', 'x' */			      \
          REF (form_float),		/* for 'E', 'e', 'F', 'f', 'G', 'g' */	      \
          REF (form_character),	/* for 'c' */				      \
          REF (form_string),	/* for 's', 'S' */			      \
          REF (form_pointer),	/* for 'p' */				      \
          REF (form_number),	/* for 'n' */				      \
          REF (form_strerror),	/* for 'm' */				      \
          REF (form_wcharacter),	/* for 'C' */				      \
          REF (form_floathex),	/* for 'A', 'a' */			      \
          REF (form_unknown),       /* for 't' */				      \
          REF (form_unknown),       /* for 'j' */				      \
          REF (form_unknown),       /* for 'I' */				      \
          REF (form_binary),	/* for 'B', 'b' */			      \
        }
    #define STEP4_TABLE							      \
        /* Step 4: processing format specifier.  */				      \
        static JUMP_TABLE_TYPE step4_jumps[31] =				      \
        {									      \
          REF (form_unknown),						      \
          REF (form_unknown),	/* for ' ' */				      \
          REF (form_unknown),	/* for '+' */				      \
          REF (form_unknown),	/* for '-' */				      \
          REF (form_unknown),	/* for '<hash>' */			      \
          REF (form_unknown),	/* for '0' */				      \
          REF (form_unknown),	/* for '\'' */				      \
          REF (form_unknown),	/* for '*' */				      \
          REF (form_unknown),	/* for '1'...'9' */			      \
          REF (form_unknown),	/* for '.' */				      \
          REF (form_unknown),	/* for 'h' */				      \
          REF (form_unknown),	/* for 'l' */				      \
          REF (form_unknown),	/* for 'L', 'q' */			      \
          REF (form_unknown),	/* for 'z', 'Z' */			      \
          REF (form_percent),	/* for '%' */				      \
          REF (form_integer),	/* for 'd', 'i' */			      \
          REF (form_unsigned),	/* for 'u' */				      \
          REF (form_octal),		/* for 'o' */				      \
          REF (form_hexa),		/* for 'X', 'x' */			      \
          REF (form_float),		/* for 'E', 'e', 'F', 'f', 'G', 'g' */	      \
          REF (form_character),	/* for 'c' */				      \
          REF (form_string),	/* for 's', 'S' */			      \
          REF (form_pointer),	/* for 'p' */				      \
          REF (form_number),	/* for 'n' */				      \
          REF (form_strerror),	/* for 'm' */				      \
          REF (form_wcharacter),	/* for 'C' */				      \
          REF (form_floathex),	/* for 'A', 'a' */			      \
          REF (form_unknown),       /* for 't' */				      \
          REF (form_unknown),       /* for 'j' */				      \
          REF (form_unknown),       /* for 'I' */				      \
          REF (form_binary),	/* for 'B', 'b' */			      \
        }
    /* Before invoking this macro, process_arg_int etc. macros have to be
       defined to extract one argument of the appropriate type.  */
    #define process_arg()						              \
          /* Start real work.  We know about all flags and modifiers and	      \
    	 now process the wanted format specifier.  */			      \
        LABEL (form_percent):						      \
          /* Write a literal "%".  */					      \
          outchar (L_('%'));						      \
          break;								      \
    									      \
        LABEL (form_integer):						      \
          /* Signed decimal integer.  */					      \
          base = 10;							      \
    									      \
          if (is_longlong)							      \
    	{								      \
    	  long long int signed_number = process_arg_long_long_int ();	      \
    	  is_negative = signed_number < 0;				      \
    	  number.longlong = is_negative ? (- signed_number) : signed_number;  \
    									      \
    	  goto LABEL (longlong_number);					      \
    	}								      \
          else								      \
    	{								      \
    	  long int signed_number;					      \
    	  if (is_long_num)						      \
    	    signed_number = process_arg_long_int ();			      \
    	  else if (is_char)						      \
    	    signed_number = (signed char) process_arg_unsigned_int ();	      \
    	  else if (!is_short)						      \
    	    signed_number = process_arg_int ();				      \
    	  else								      \
    	    signed_number = (short int) process_arg_unsigned_int ();	      \
    									      \
    	  is_negative = signed_number < 0;				      \
    	  number.word = is_negative ? (- signed_number) : signed_number;      \
    									      \
    	  goto LABEL (number);						      \
    	}								      \
          /* NOTREACHED */							      \
    									      \
        LABEL (form_unsigned):						      \
          /* Unsigned decimal integer.  */					      \
          base = 10;							      \
          goto LABEL (unsigned_number);					      \
          /* NOTREACHED */							      \
    									      \
        LABEL (form_octal):							      \
          /* Unsigned octal integer.  */					      \
          base = 8;								      \
          goto LABEL (unsigned_number);					      \
          /* NOTREACHED */							      \
    									      \
        LABEL (form_hexa):							      \
          /* Unsigned hexadecimal integer.  */				      \
          base = 16;							      \
          goto LABEL (unsigned_number);					      \
          /* NOTREACHED */							      \
    									      \
        LABEL (form_binary):						      \
          /* Unsigned binary integer.  */					      \
          base = 2;								      \
          goto LABEL (unsigned_number);					      \
          /* NOTREACHED */							      \
    									      \
        LABEL (unsigned_number):	  /* Unsigned number of base BASE.  */	      \
    									      \
          /* ISO specifies the `+' and ` ' flags only for signed		      \
    	 conversions.  */						      \
          is_negative = 0;							      \
          showsign = 0;							      \
          space = 0;							      \
    									      \
          if (is_longlong)							      \
    	{								      \
    	  number.longlong = process_arg_unsigned_long_long_int ();	      \
    									      \
    	LABEL (longlong_number):					      \
    	  if (prec < 0)							      \
    	    /* Supply a default precision if none was given.  */	      \
    	    prec = 1;							      \
    	  else								      \
    	    /* We have to take care for the '0' flag.  If a precision	      \
    	       is given it must be ignored.  */				      \
    	    pad = L_(' ');						      \
    									      \
    	  /* If the precision is 0 and the number is 0 nothing has to	      \
    	     be written for the number, except for the 'o' format in	      \
    	     alternate form.  */					      \
    	  if (prec == 0 && number.longlong == 0)			      \
    	    {								      \
    	      string = workend;						      \
    	      if (base == 8 && alt)					      \
    		*--string = L_('0');					      \
    	    }								      \
    	  else								      \
    	    {								      \
    	      /* Put the number in WORK.  */				      \
    	      string = _itoa (number.longlong, workend, base,		      \
    			      spec == L_('X'));				      \
    	      if (group && grouping)					      \
    		string = group_number (work_buffer, string, workend,	      \
    				       grouping, thousands_sep);	      \
    	      if (use_outdigits && base == 10)				      \
    		string = _i18n_number_rewrite (string, workend, workend);     \
    	    }								      \
    	  /* Simplify further test for num != 0.  */			      \
    	  number.word = number.longlong != 0;				      \
    	}								      \
          else								      \
    	{								      \
    	  if (is_long_num)						      \
    	    number.word = process_arg_unsigned_long_int ();		      \
    	  else if (is_char)						      \
    	    number.word = (unsigned char) process_arg_unsigned_int ();	      \
    	  else if (!is_short)						      \
    	    number.word = process_arg_unsigned_int ();			      \
    	  else								      \
    	    number.word = (unsigned short int) process_arg_unsigned_int ();   \
    									      \
    	LABEL (number):							      \
    	  if (prec < 0)							      \
    	    /* Supply a default precision if none was given.  */	      \
    	    prec = 1;							      \
    	  else								      \
    	    /* We have to take care for the '0' flag.  If a precision	      \
    	       is given it must be ignored.  */				      \
    	    pad = L_(' ');						      \
    									      \
    	  /* If the precision is 0 and the number is 0 nothing has to	      \
    	     be written for the number, except for the 'o' format in	      \
    	     alternate form.  */					      \
    	  if (prec == 0 && number.word == 0)				      \
    	    {								      \
    	      string = workend;						      \
    	      if (base == 8 && alt)					      \
    		*--string = L_('0');					      \
    	    }								      \
    	  else								      \
    	    {								      \
    	      /* Put the number in WORK.  */				      \
    	      string = _itoa_word (number.word, workend, base,		      \
    				   spec == L_('X'));			      \
    	      if (group && grouping)					      \
    		string = group_number (work_buffer, string, workend,	      \
    				       grouping, thousands_sep);	      \
    	      if (use_outdigits && base == 10)				      \
    		string = _i18n_number_rewrite (string, workend, workend);     \
    	    }								      \
    	}								      \
    									      \
          if (prec <= workend - string && number.word != 0 && alt && base == 8)   \
    	/* Add octal marker.  */					      \
    	*--string = L_('0');						      \
    									      \
          prec = MAX (0, prec - (workend - string));			      \
    									      \
          if (!left)							      \
    	{								      \
    	  width -= workend - string + prec;				      \
    									      \
    	  if (number.word != 0 && alt && (base == 16 || base == 2))	      \
    	    /* Account for 0X, 0x, 0B or 0b hex or binary marker.  */	      \
    	    width -= 2;							      \
    									      \
    	  if (is_negative || showsign || space)				      \
    	    --width;							      \
    									      \
    	  if (pad == L_(' '))						      \
    	    {								      \
    	      PAD (L_(' '));						      \
    	      width = 0;						      \
    	    }								      \
    									      \
    	  if (is_negative)						      \
    	    outchar (L_('-'));						      \
    	  else if (showsign)						      \
    	    outchar (L_('+'));						      \
    	  else if (space)						      \
    	    outchar (L_(' '));						      \
    									      \
    	  if (number.word != 0 && alt && (base == 16 || base == 2))	      \
    	    {								      \
    	      outchar (L_('0'));					      \
    	      outchar (spec);						      \
    	    }								      \
    									      \
    	  width += prec;						      \
    	  PAD (L_('0'));						      \
    									      \
    	  outstring (string, workend - string);				      \
    									      \
    	  break;							      \
    	}								      \
          else								      \
    	{								      \
    	  if (is_negative)						      \
    	    {								      \
    	      outchar (L_('-'));					      \
    	      --width;							      \
    	    }								      \
    	  else if (showsign)						      \
    	    {								      \
    	      outchar (L_('+'));					      \
    	      --width;							      \
    	    }								      \
    	  else if (space)						      \
    	    {								      \
    	      outchar (L_(' '));					      \
    	      --width;							      \
    	    }								      \
    									      \
    	  if (number.word != 0 && alt && (base == 16 || base == 2))	      \
    	    {								      \
    	      outchar (L_('0'));					      \
    	      outchar (spec);						      \
    	      width -= 2;						      \
    	    }								      \
    									      \
    	  width -= workend - string + prec;				      \
    									      \
    	  if (prec > 0)							      \
    	    {								      \
    	      int temp = width;						      \
    	      width = prec;						      \
    	      PAD (L_('0'));						      \
    	      width = temp;						      \
    	    }								      \
    									      \
    	  outstring (string, workend - string);				      \
    									      \
    	  PAD (L_(' '));						      \
    	  break;							      \
    	}								      \
    									      \
        LABEL (form_pointer):						      \
          /* Generic pointer.  */						      \
          {									      \
    	const void *ptr = process_arg_pointer ();			      \
    	if (ptr != NULL)						      \
    	  {								      \
    	    /* If the pointer is not NULL, write it as a %#x spec.  */	      \
    	    base = 16;							      \
    	    number.word = (unsigned long int) ptr;			      \
    	    is_negative = 0;						      \
    	    alt = 1;							      \
    	    group = 0;							      \
    	    spec = L_('x');						      \
    	    goto LABEL (number);					      \
    	  }								      \
    	else								      \
    	  {								      \
    	    /* Write "(nil)" for a nil pointer.  */			      \
    	    string = (CHAR_T *) L_("(nil)");				      \
    	    /* Make sure the full string "(nil)" is printed.  */	      \
    	    if (prec < 5)						      \
    	      prec = 5;							      \
    	    /* This is a wide string iff compiling wprintf.  */		      \
    	    is_long = sizeof (CHAR_T) > 1;				      \
    	    goto LABEL (print_string);					      \
    	  }								      \
          }									      \
          /* NOTREACHED */							      \
    									      \
        LABEL (form_number):						      \
          if ((mode_flags & PRINTF_FORTIFY) != 0)				      \
    	{								      \
    	  if (! readonly_format)					      \
    	    {								      \
    	      extern int __readonly_area (const void *, size_t)		      \
    		attribute_hidden;					      \
    	      readonly_format						      \
    		= __readonly_area (format, ((STR_LEN (format) + 1)	      \
    					    * sizeof (CHAR_T)));	      \
    	    }								      \
    	  if (readonly_format < 0)					      \
    	    __libc_fatal ("*** %n in writable segment detected ***\n");	      \
    	}								      \
          /* Answer the count of characters written.  */			      \
          void *ptrptr = process_arg_pointer ();				      \
          if (is_longlong)							      \
    	*(long long int *) ptrptr = done;				      \
          else if (is_long_num)						      \
    	*(long int *) ptrptr = done;					      \
          else if (is_char)							      \
    	*(char *) ptrptr = done;					      \
          else if (!is_short)						      \
    	*(int *) ptrptr = done;						      \
          else								      \
    	*(short int *) ptrptr = done;					      \
          break;								      \
    									      \
        LABEL (form_strerror):						      \
          /* Print description of error ERRNO.  */				      \
          if (alt)								      \
    	string = (CHAR_T *) __get_errname (save_errno);			      \
          else								      \
    	string = (CHAR_T *) __strerror_r (save_errno, (char *) work_buffer,   \
    					  WORK_BUFFER_SIZE * sizeof (CHAR_T));\
          if (string == NULL)						\
    	{								      \
              /* Print as a decimal number. */				      \
              base = 10;							      \
    	  is_negative = save_errno < 0;					      \
    	  number.word = save_errno;					      \
    	  if (is_negative)						      \
    	    number.word = -number.word;					      \
    	  goto LABEL (number);						      \
    	}								      \
          else								      \
    	{								      \
    	  is_long = 0;	/* This is no wide-char string.  */		      \
    	  goto LABEL (print_string);					      \
    	}
    #ifdef COMPILE_WPRINTF
    # define process_string_arg()						      \
        LABEL (form_character):						      \
          /* Character.  */							      \
          if (is_long)							      \
    	goto LABEL (form_wcharacter);					      \
          --width;	/* Account for the character itself.  */		      \
          if (!left)							      \
    	PAD (L' ');							      \
          outchar (__btowc ((unsigned char) process_arg_int ())); /* Promoted. */ \
          if (left)								      \
    	PAD (L' ');							      \
          break;								      \
    									      \
        LABEL (form_wcharacter):						      \
          {									      \
    	/* Wide character.  */						      \
    	--width;							      \
    	if (!left)							      \
    	  PAD (L' ');							      \
    	outchar (process_arg_wchar_t ());				      \
    	if (left)							      \
    	  PAD (L' ');							      \
          }									      \
          break;								      \
    									      \
        LABEL (form_string):						      \
          {									      \
    	size_t len;							      \
    									      \
    	/* The string argument could in fact be `char *' or `wchar_t *'.      \
    	   But this should not make a difference here.  */		      \
    	string = (CHAR_T *) process_arg_wstring ();			      \
    									      \
    	/* Entry point for printing other strings.  */			      \
          LABEL (print_string):						      \
    									      \
    	if (string == NULL)						      \
    	  {								      \
    	    /* Write "(null)" if there's space.  */			      \
    	    if (prec == -1 || prec >= (int) array_length (null) - 1)          \
    	      {								      \
    		string = (CHAR_T *) null;				      \
    		len = array_length (null) - 1;				      \
    	      }								      \
    	    else							      \
    	      {								      \
    		string = (CHAR_T *) L"";				      \
    		len = 0;						      \
    	      }								      \
    	  }								      \
    	else if (!is_long && spec != L_('S'))				      \
    	  {								      \
    	    done = outstring_converted_wide_string			      \
    	      (s, (const char *) string, prec, width, left, done);	      \
    	    if (done < 0)						      \
    	      goto all_done;						      \
    	    /* The padding has already been written.  */		      \
    	    break;							      \
    	  }								      \
    	else								      \
    	  {								      \
    	    if (prec != -1)						      \
    	      /* Search for the end of the string, but don't search past      \
    		 the length specified by the precision.  */		      \
    	      len = __wcsnlen (string, prec);				      \
    	    else							      \
    	      len = __wcslen (string);					      \
    	  }								      \
    									      \
    	if ((width -= len) < 0)						      \
    	  {								      \
    	    outstring (string, len);					      \
    	    break;							      \
    	  }								      \
    									      \
    	if (!left)							      \
    	  PAD (L' ');							      \
    	outstring (string, len);					      \
    	if (left)							      \
    	  PAD (L' ');							      \
          }									      \
          break;
    #else
    # define process_string_arg()						      \
        LABEL (form_character):						      \
          /* Character.  */							      \
          if (is_long)							      \
    	goto LABEL (form_wcharacter);					      \
          --width;	/* Account for the character itself.  */		      \
          if (!left)							      \
    	PAD (' ');							      \
          outchar ((unsigned char) process_arg_int ()); /* Promoted.  */	      \
          if (left)								      \
    	PAD (' ');							      \
          break;								      \
    									      \
        LABEL (form_wcharacter):						      \
          {									      \
    	/* Wide character.  */						      \
    	char buf[MB_LEN_MAX];						      \
    	mbstate_t mbstate;						      \
    	size_t len;							      \
    									      \
    	memset (&mbstate, '\0', sizeof (mbstate_t));			      \
    	len = __wcrtomb (buf, process_arg_wchar_t (), &mbstate);	      \
    	if (len == (size_t) -1)						      \
    	  {								      \
    	    /* Something went wrong during the conversion.  Bail out.  */     \
    	    done = -1;							      \
    	    goto all_done;						      \
    	  }								      \
    	width -= len;							      \
    	if (!left)							      \
    	  PAD (' ');							      \
    	outstring (buf, len);						      \
    	if (left)							      \
    	  PAD (' ');							      \
          }									      \
          break;								      \
    									      \
        LABEL (form_string):						      \
          {									      \
    	size_t len;							      \
    									      \
    	/* The string argument could in fact be `char *' or `wchar_t *'.      \
    	   But this should not make a difference here.  */		      \
    	string = (char *) process_arg_string ();			      \
    									      \
    	/* Entry point for printing other strings.  */			      \
          LABEL (print_string):						      \
    									      \
    	if (string == NULL)						      \
    	  {								      \
    	    /* Write "(null)" if there's space.  */			      \
    	    if (prec == -1 || prec >= (int) sizeof (null) - 1)		      \
    	      {								      \
    		string = (char *) null;					      \
    		len = sizeof (null) - 1;				      \
    	      }								      \
    	    else							      \
    	      {								      \
    		string = (char *) "";					      \
    		len = 0;						      \
    	      }								      \
    	  }								      \
    	else if (!is_long && spec != L_('S'))				      \
    	  {								      \
    	    if (prec != -1)						      \
    	      /* Search for the end of the string, but don't search past      \
    		 the length (in bytes) specified by the precision.  */	      \
    	      len = __strnlen (string, prec);				      \
    	    else							      \
    	      len = strlen (string);					      \
    	  }								      \
    	else								      \
    	  {								      \
    	    done = outstring_converted_wide_string			      \
    	      (s, (const wchar_t *) string, prec, width, left, done);	      \
    	    if (done < 0)						      \
    	      goto all_done;						      \
    	    /* The padding has already been written.  */		      \
    	    break;							      \
    	  }								      \
    									      \
    	if ((width -= len) < 0)						      \
    	  {								      \
    	    outstring (string, len);					      \
    	    break;							      \
    	  }								      \
    									      \
    	if (!left)							      \
    	  PAD (' ');							      \
    	outstring (string, len);					      \
    	if (left)							      \
    	  PAD (' ');							      \
          }									      \
          break;
    #endif
    /* Helper function to provide temporary buffering for unbuffered streams.  */
    static int buffered_vfprintf (FILE *stream, const CHAR_T *fmt, va_list,
    			      unsigned int)
         __THROW __attribute__ ((noinline));
    /* Handle positional format specifiers.  */
    static int printf_positional (FILE *s,
    			      const CHAR_T *format, int readonly_format,
    			      va_list ap, va_list *ap_savep, int done,
    			      int nspecs_done, const UCHAR_T *lead_str_end,
    			      CHAR_T *work_buffer, int save_errno,
    			      const char *grouping,
    			      THOUSANDS_SEP_T thousands_sep,
    			      unsigned int mode_flags);
    /* Handle unknown format specifier.  */
    static int printf_unknown (FILE *, const struct printf_info *,
    			   const void *const *) __THROW;
    /* Group digits of number string.  */
    static CHAR_T *group_number (CHAR_T *, CHAR_T *, CHAR_T *, const char *,
    			     THOUSANDS_SEP_T);
    /* The function itself.  */
    int
    vfprintf (FILE *s, const CHAR_T *format, va_list ap, unsigned int mode_flags)
    {
      /* The character used as thousands separator.  */
      THOUSANDS_SEP_T thousands_sep = 0;
      /* The string describing the size of groups of digits.  */
      const char *grouping;
      /* Place to accumulate the result.  */
      int done;
      /* Current character in format string.  */
      const UCHAR_T *f;
      /* End of leading constant string.  */
      const UCHAR_T *lead_str_end;
      /* Points to next format specifier.  */
      const UCHAR_T *end_of_spec;
      /* Buffer intermediate results.  */
      CHAR_T work_buffer[WORK_BUFFER_SIZE];
      CHAR_T *workend;
      /* We have to save the original argument pointer.  */
      va_list ap_save;
      /* Count number of specifiers we already processed.  */
      int nspecs_done;
      /* For the %m format we may need the current `errno' value.  */
      int save_errno = errno;
      /* 1 if format is in read-only memory, -1 if it is in writable memory,
         0 if unknown.  */
      int readonly_format = 0;
      /* Orient the stream.  */
    #ifdef ORIENT
      ORIENT;
    #endif
      /* Sanity check of arguments.  */
      ARGCHECK (s, format);
    #ifdef ORIENT
      /* Check for correct orientation.  */
      if (_IO_vtable_offset (s) == 0
          && _IO_fwide (s, sizeof (CHAR_T) == 1 ? -1 : 1)
          != (sizeof (CHAR_T) == 1 ? -1 : 1))
        /* The stream is already oriented otherwise.  */
        return EOF;
    #endif
      if (UNBUFFERED_P (s))
        /* Use a helper function which will allocate a local temporary buffer
           for the stream and then call us again.  */
        return buffered_vfprintf (s, format, ap, mode_flags);
      /* Initialize local variables.  */
      done = 0;
      grouping = (const char *) -1;
    #ifdef __va_copy
      /* This macro will be available soon in gcc's <stdarg.h>.  We need it
         since on some systems `va_list' is not an integral type.  */
      __va_copy (ap_save, ap);
    #else
      ap_save = ap;
    #endif
      nspecs_done = 0;
    #ifdef COMPILE_WPRINTF
      /* Find the first format specifier.  */
      f = lead_str_end = __find_specwc ((const UCHAR_T *) format);
    #else
      /* Find the first format specifier.  */
      f = lead_str_end = __find_specmb ((const UCHAR_T *) format);
    #endif
      /* Lock stream.  */
      _IO_cleanup_region_start ((void (*) (void *)) &_IO_funlockfile, s);
      _IO_flockfile (s);
      /* Write the literal text before the first format.  */
      outstring ((const UCHAR_T *) format,
    	     lead_str_end - (const UCHAR_T *) format);
      /* If we only have to print a simple string, return now.  */
      if (*f == L_('\0'))
        goto all_done;
      /* Use the slow path in case any printf handler is registered.  */
      if (__glibc_unlikely (__printf_function_table != NULL
    			|| __printf_modifier_table != NULL
    			|| __printf_va_arg_table != NULL))
        goto do_positional;
      /* Process whole format string.  */
      do
        {
          STEP0_3_TABLE;
          STEP4_TABLE;
          int is_negative;	/* Flag for negative number.  */
          union
          {
    	unsigned long long int longlong;
    	unsigned long int word;
          } number;
          int base;
          union printf_arg the_arg;
          CHAR_T *string;	/* Pointer to argument string.  */
          int alt = 0;	/* Alternate format.  */
          int space = 0;	/* Use space prefix if no sign is needed.  */
          int left = 0;	/* Left-justify output.  */
          int showsign = 0;	/* Always begin with plus or minus sign.  */
          int group = 0;	/* Print numbers according grouping rules.  */
          /* Argument is long double/long long int.  Only used if
    	 double/long double or long int/long long int are distinct.  */
          int is_long_double __attribute__ ((unused)) = 0;
          int is_short = 0;	/* Argument is short int.  */
          int is_long = 0;	/* Argument is long int.  */
          int is_char = 0;	/* Argument is promoted (unsigned) char.  */
          int width = 0;	/* Width of output; 0 means none specified.  */
          int prec = -1;	/* Precision of output; -1 means none specified.  */
          /* This flag is set by the 'I' modifier and selects the use of the
    	 `outdigits' as determined by the current locale.  */
          int use_outdigits = 0;
          UCHAR_T pad = L_(' ');/* Padding character.  */
          CHAR_T spec;
          workend = work_buffer + WORK_BUFFER_SIZE;
          /* Get current character in format string.  */
          JUMP (*++f, step0_jumps);
          /* ' ' flag.  */
        LABEL (flag_space):
          space = 1;
          JUMP (*++f, step0_jumps);
          /* '+' flag.  */
        LABEL (flag_plus):
          showsign = 1;
          JUMP (*++f, step0_jumps);
          /* The '-' flag.  */
        LABEL (flag_minus):
          left = 1;
          pad = L_(' ');
          JUMP (*++f, step0_jumps);
          /* The '#' flag.  */
        LABEL (flag_hash):
          alt = 1;
          JUMP (*++f, step0_jumps);
          /* The '0' flag.  */
        LABEL (flag_zero):
          if (!left)
    	pad = L_('0');
          JUMP (*++f, step0_jumps);
          /* The '\'' flag.  */
        LABEL (flag_quote):
          group = 1;
          if (grouping == (const char *) -1)
    	{
    #ifdef COMPILE_WPRINTF
    	  thousands_sep = _NL_CURRENT_WORD (LC_NUMERIC,
    					    _NL_NUMERIC_THOUSANDS_SEP_WC);
    #else
    	  thousands_sep = _NL_CURRENT (LC_NUMERIC, THOUSANDS_SEP);
    #endif
    	  grouping = _NL_CURRENT (LC_NUMERIC, GROUPING);
    	  if (*grouping == '\0' || *grouping == CHAR_MAX
    #ifdef COMPILE_WPRINTF
    	      || thousands_sep == L'\0'
    #else
    	      || *thousands_sep == '\0'
    #endif
    	      )
    	    grouping = NULL;
    	}
          JUMP (*++f, step0_jumps);
        LABEL (flag_i18n):
          use_outdigits = 1;
          JUMP (*++f, step0_jumps);
          /* Get width from argument.  */
        LABEL (width_asterics):
          {
    	const UCHAR_T *tmp;	/* Temporary value.  */
    	tmp = ++f;
    	if (ISDIGIT (*tmp))
    	  {
    	    int pos = read_int (&tmp);
    	    if (pos == -1)
    	      {
    		__set_errno (EOVERFLOW);
    		done = -1;
    		goto all_done;
    	      }
    	    if (pos && *tmp == L_('$'))
    	      /* The width comes from a positional parameter.  */
    	      goto do_positional;
    	  }
    	width = va_arg (ap, int);
    	/* Negative width means left justified.  */
    	if (width < 0)
    	  {
    	    width = -width;
    	    pad = L_(' ');
    	    left = 1;
    	  }
          }
          JUMP (*f, step1_jumps);
          /* Given width in format string.  */
        LABEL (width):
          width = read_int (&f);
          if (__glibc_unlikely (width == -1))
    	{
    	  __set_errno (EOVERFLOW);
    	  done = -1;
    	  goto all_done;
    	}
          if (*f == L_('$'))
    	/* Oh, oh.  The argument comes from a positional parameter.  */
    	goto do_positional;
          JUMP (*f, step1_jumps);
        LABEL (precision):
          ++f;
          if (*f == L_('*'))
    	{
    	  const UCHAR_T *tmp;	/* Temporary value.  */
    	  tmp = ++f;
    	  if (ISDIGIT (*tmp))
    	    {
    	      int pos = read_int (&tmp);
    	      if (pos == -1)
    		{
    		  __set_errno (EOVERFLOW);
    		  done = -1;
    		  goto all_done;
    		}
    	      if (pos && *tmp == L_('$'))
    		/* The precision comes from a positional parameter.  */
    		goto do_positional;
    	    }
    	  prec = va_arg (ap, int);
    	  /* If the precision is negative the precision is omitted.  */
    	  if (prec < 0)
    	    prec = -1;
    	}
          else if (ISDIGIT (*f))
    	{
    	  prec = read_int (&f);
    	  /* The precision was specified in this case as an extremely
    	     large positive value.  */
    	  if (prec == -1)
    	    {
    	      __set_errno (EOVERFLOW);
    	      done = -1;
    	      goto all_done;
    	    }
    	}
          else
    	prec = 0;
          JUMP (*f, step2_jumps);
          /* Process 'h' modifier.  There might another 'h' following.  */
        LABEL (mod_half):
          is_short = 1;
          JUMP (*++f, step3a_jumps);
          /* Process 'hh' modifier.  */
        LABEL (mod_halfhalf):
          is_short = 0;
          is_char = 1;
          JUMP (*++f, step4_jumps);
          /* Process 'l' modifier.  There might another 'l' following.  */
        LABEL (mod_long):
          is_long = 1;
          JUMP (*++f, step3b_jumps);
          /* Process 'L', 'q', or 'll' modifier.  No other modifier is
    	 allowed to follow.  */
        LABEL (mod_longlong):
          is_long_double = 1;
          is_long = 1;
          JUMP (*++f, step4_jumps);
        LABEL (mod_size_t):
          is_long_double = sizeof (size_t) > sizeof (unsigned long int);
          is_long = sizeof (size_t) > sizeof (unsigned int);
          JUMP (*++f, step4_jumps);
        LABEL (mod_ptrdiff_t):
          is_long_double = sizeof (ptrdiff_t) > sizeof (unsigned long int);
          is_long = sizeof (ptrdiff_t) > sizeof (unsigned int);
          JUMP (*++f, step4_jumps);
        LABEL (mod_intmax_t):
          is_long_double = sizeof (intmax_t) > sizeof (unsigned long int);
          is_long = sizeof (intmax_t) > sizeof (unsigned int);
          JUMP (*++f, step4_jumps);
          /* Process current format.  */
          while (1)
    	{
    #define process_arg_int() va_arg (ap, int)
    #define process_arg_long_int() va_arg (ap, long int)
    #define process_arg_long_long_int() va_arg (ap, long long int)
    #define process_arg_pointer() va_arg (ap, void *)
    #define process_arg_string() va_arg (ap, const char *)
    #define process_arg_unsigned_int() va_arg (ap, unsigned int)
    #define process_arg_unsigned_long_int() va_arg (ap, unsigned long int)
    #define process_arg_unsigned_long_long_int() va_arg (ap, unsigned long long int)
    #define process_arg_wchar_t() va_arg (ap, wchar_t)
    #define process_arg_wstring() va_arg (ap, const wchar_t *)
    	  process_arg ();
    	  process_string_arg ();
    #undef process_arg_int
    #undef process_arg_long_int
    #undef process_arg_long_long_int
    #undef process_arg_pointer
    #undef process_arg_string
    #undef process_arg_unsigned_int
    #undef process_arg_unsigned_long_int
    #undef process_arg_unsigned_long_long_int
    #undef process_arg_wchar_t
    #undef process_arg_wstring
    	LABEL (form_float):
    	LABEL (form_floathex):
    	  {
    	    if (__glibc_unlikely ((mode_flags & PRINTF_LDBL_IS_DBL) != 0))
    	      is_long_double = 0;
    	    struct printf_info info =
    	      {
    		.prec = prec,
    		.width = width,
    		.spec = spec,
    		.is_long_double = is_long_double,
    		.is_short = is_short,
    		.is_long = is_long,
    		.alt = alt,
    		.space = space,
    		.left = left,
    		.showsign = showsign,
    		.group = group,
    		.pad = pad,
    		.extra = 0,
    		.i18n = use_outdigits,
    		.wide = sizeof (CHAR_T) != 1,
    		.is_binary128 = 0
    	      };
    	    PARSE_FLOAT_VA_ARG_EXTENDED (info);
    	    const void *ptr = &the_arg;
    	    int function_done = __printf_fp_spec (s, &info, &ptr);
    	    if (function_done < 0)
    	      {
    		done = -1;
    		goto all_done;
    	      }
    	    done_add (function_done);
    	  }
    	  break;
    	LABEL (form_unknown):
    	  if (spec == L_('\0'))
    	    {
    	      /* The format string ended before the specifier is complete.  */
    	      __set_errno (EINVAL);
    	      done = -1;
    	      goto all_done;
    	    }
    	  /* If we are in the fast loop force entering the complicated
    	     one.  */
    	  goto do_positional;
    	}
          /* The format is correctly handled.  */
          ++nspecs_done;
          /* Look for next format specifier.  */
    #ifdef COMPILE_WPRINTF
          f = __find_specwc ((end_of_spec = ++f));
    #else
          f = __find_specmb ((end_of_spec = ++f));
    #endif
          /* Write the following constant string.  */
          outstring (end_of_spec, f - end_of_spec);
        }
      while (*f != L_('\0'));
      /* Unlock stream and return.  */
      goto all_done;
      /* Hand off processing for positional parameters.  */
    do_positional:
      done = printf_positional (s, format, readonly_format, ap, &ap_save,
    			    done, nspecs_done, lead_str_end, work_buffer,
    			    save_errno, grouping, thousands_sep, mode_flags);
     all_done:
      /* Unlock the stream.  */
      _IO_funlockfile (s);
      _IO_cleanup_region_end (0);
      return done;
    }
    
    static int
    printf_positional (FILE *s, const CHAR_T *format, int readonly_format,
    		   va_list ap, va_list *ap_savep, int done, int nspecs_done,
    		   const UCHAR_T *lead_str_end,
    		   CHAR_T *work_buffer, int save_errno,
    		   const char *grouping, THOUSANDS_SEP_T thousands_sep,
    		   unsigned int mode_flags)
    {
      /* For positional argument handling.  */
      struct scratch_buffer specsbuf;
      scratch_buffer_init (&specsbuf);
      struct printf_spec *specs = specsbuf.data;
      size_t specs_limit = specsbuf.length / sizeof (specs[0]);
      /* Used as a backing store for args_value, args_size, args_type
         below.  */
      struct scratch_buffer argsbuf;
      scratch_buffer_init (&argsbuf);
      /* Array with information about the needed arguments.  This has to
         be dynamically extensible.  */
      size_t nspecs = 0;
      /* The number of arguments the format string requests.  This will
         determine the size of the array needed to store the argument
         attributes.  */
      size_t nargs = 0;
      /* Positional parameters refer to arguments directly.  This could
         also determine the maximum number of arguments.  Track the
         maximum number.  */
      size_t max_ref_arg = 0;
      /* Just a counter.  */
      size_t cnt;
      if (grouping == (const char *) -1)
        {
    #ifdef COMPILE_WPRINTF
          thousands_sep = _NL_CURRENT_WORD (LC_NUMERIC,
    					_NL_NUMERIC_THOUSANDS_SEP_WC);
    #else
          thousands_sep = _NL_CURRENT (LC_NUMERIC, THOUSANDS_SEP);
    #endif
          grouping = _NL_CURRENT (LC_NUMERIC, GROUPING);
          if (*grouping == '\0' || *grouping == CHAR_MAX)
    	grouping = NULL;
        }
      for (const UCHAR_T *f = lead_str_end; *f != L_('\0');
           f = specs[nspecs++].next_fmt)
        {
          if (nspecs == specs_limit)
    	{
    	  if (!scratch_buffer_grow_preserve (&specsbuf))
    	    {
    	      done = -1;
    	      goto all_done;
    	    }
    	  specs = specsbuf.data;
    	  specs_limit = specsbuf.length / sizeof (specs[0]);
    	}
          /* Parse the format specifier.  */
    #ifdef COMPILE_WPRINTF
          nargs += __parse_one_specwc (f, nargs, &specs[nspecs], &max_ref_arg);
    #else
          nargs += __parse_one_specmb (f, nargs, &specs[nspecs], &max_ref_arg);
    #endif
        }
      /* Determine the number of arguments the format string consumes.  */
      nargs = MAX (nargs, max_ref_arg);
      union printf_arg *args_value;
      int *args_size;
      int *args_type;
      {
        /* Calculate total size needed to represent a single argument
           across all three argument-related arrays.  */
        size_t bytes_per_arg
          = sizeof (*args_value) + sizeof (*args_size) + sizeof (*args_type);
        if (!scratch_buffer_set_array_size (&argsbuf, nargs, bytes_per_arg))
          {
    	done = -1;
    	goto all_done;
          }
        args_value = argsbuf.data;
        /* Set up the remaining two arrays to each point past the end of
           the prior array, since space for all three has been allocated
           now.  */
        args_size = &args_value[nargs].pa_int;
        args_type = &args_size[nargs];
        memset (args_type, (mode_flags & PRINTF_FORTIFY) != 0 ? '\xff' : '\0',
    	    nargs * sizeof (*args_type));
      }
      /* XXX Could do sanity check here: If any element in ARGS_TYPE is
         still zero after this loop, format is invalid.  For now we
         simply use 0 as the value.  */
      /* Fill in the types of all the arguments.  */
      for (cnt = 0; cnt < nspecs; ++cnt)
        {
          /* If the width is determined by an argument this is an int.  */
          if (specs[cnt].width_arg != -1)
    	args_type[specs[cnt].width_arg] = PA_INT;
          /* If the precision is determined by an argument this is an int.  */
          if (specs[cnt].prec_arg != -1)
    	args_type[specs[cnt].prec_arg] = PA_INT;
          switch (specs[cnt].ndata_args)
    	{
    	case 0:		/* No arguments.  */
    	  break;
    	case 1:		/* One argument; we already have the
    			   type and size.  */
    	  args_type[specs[cnt].data_arg] = specs[cnt].data_arg_type;
    	  args_size[specs[cnt].data_arg] = specs[cnt].size;
    	  break;
    	default:
    	  /* We have more than one argument for this format spec.
    	     We must call the arginfo function again to determine
    	     all the types.  */
    	  (void) (*__printf_arginfo_table[specs[cnt].info.spec])
    	    (&specs[cnt].info,
    	     specs[cnt].ndata_args, &args_type[specs[cnt].data_arg],
    	     &args_size[specs[cnt].data_arg]);
    	  break;
    	}
        }
      /* Now we know all the types and the order.  Fill in the argument
         values.  */
      for (cnt = 0; cnt < nargs; ++cnt)
        switch (args_type[cnt])
          {
    #define T(tag, mem, type)				\
    	case tag:					\
    	  args_value[cnt].mem = va_arg (*ap_savep, type); \
    	  break
    	T (PA_WCHAR, pa_wchar, wint_t);
          case PA_CHAR:				/* Promoted.  */
          case PA_INT|PA_FLAG_SHORT:		/* Promoted.  */
    #if LONG_MAX == INT_MAX
          case PA_INT|PA_FLAG_LONG:
    #endif
    	T (PA_INT, pa_int, int);
    #if LONG_MAX == LONG_LONG_MAX
          case PA_INT|PA_FLAG_LONG:
    #endif
    	T (PA_INT|PA_FLAG_LONG_LONG, pa_long_long_int, long long int);
    #if LONG_MAX != INT_MAX && LONG_MAX != LONG_LONG_MAX
    # error "he?"
    #endif
          case PA_FLOAT:				/* Promoted.  */
    	T (PA_DOUBLE, pa_double, double);
          case PA_DOUBLE|PA_FLAG_LONG_DOUBLE:
    	if (__glibc_unlikely ((mode_flags & PRINTF_LDBL_IS_DBL) != 0))
    	  {
    	    args_value[cnt].pa_double = va_arg (*ap_savep, double);
    	    args_type[cnt] &= ~PA_FLAG_LONG_DOUBLE;
    	  }
    #if __HAVE_FLOAT128_UNLIKE_LDBL
    	else if ((mode_flags & PRINTF_LDBL_USES_FLOAT128) != 0)
    	  args_value[cnt].pa_float128 = va_arg (*ap_savep, _Float128);
    #endif
    	else
    	  args_value[cnt].pa_long_double = va_arg (*ap_savep, long double);
    	break;
          case PA_STRING:				/* All pointers are the same */
          case PA_WSTRING:			/* All pointers are the same */
    	T (PA_POINTER, pa_pointer, void *);
    #undef T
          default:
    	if ((args_type[cnt] & PA_FLAG_PTR) != 0)
    	  args_value[cnt].pa_pointer = va_arg (*ap_savep, void *);
    	else if (__glibc_unlikely (__printf_va_arg_table != NULL)
    		 && __printf_va_arg_table[args_type[cnt] - PA_LAST] != NULL)
    	  {
    	    args_value[cnt].pa_user = alloca (args_size[cnt]);
    	    (*__printf_va_arg_table[args_type[cnt] - PA_LAST])
    	      (args_value[cnt].pa_user, ap_savep);
    	  }
    	else
    	  memset (&args_value[cnt], 0, sizeof (args_value[cnt]));
    	break;
          case -1:
    	/* Error case.  Not all parameters appear in N$ format
    	   strings.  We have no way to determine their type.  */
    	assert ((mode_flags & PRINTF_FORTIFY) != 0);
    	__libc_fatal ("*** invalid %N$ use detected ***\n");
          }
      /* Now walk through all format specifiers and process them.  */
      for (; (size_t) nspecs_done < nspecs; ++nspecs_done)
        {
          STEP4_TABLE;
          int is_negative;
          union
          {
    	unsigned long long int longlong;
    	unsigned long int word;
          } number;
          int base;
          CHAR_T *string;		/* Pointer to argument string.  */
          /* Fill variables from values in struct.  */
          int alt = specs[nspecs_done].info.alt;
          int space = specs[nspecs_done].info.space;
          int left = specs[nspecs_done].info.left;
          int showsign = specs[nspecs_done].info.showsign;
          int group = specs[nspecs_done].info.group;
          int is_long_double __attribute__ ((unused))
    	= specs[nspecs_done].info.is_long_double;
          int is_short = specs[nspecs_done].info.is_short;
          int is_char = specs[nspecs_done].info.is_char;
          int is_long = specs[nspecs_done].info.is_long;
          int width = specs[nspecs_done].info.width;
          int prec = specs[nspecs_done].info.prec;
          int use_outdigits = specs[nspecs_done].info.i18n;
          char pad = specs[nspecs_done].info.pad;
          CHAR_T spec = specs[nspecs_done].info.spec;
          CHAR_T *workend = work_buffer + WORK_BUFFER_SIZE;
          /* Fill in last information.  */
          if (specs[nspecs_done].width_arg != -1)
    	{
    	  /* Extract the field width from an argument.  */
    	  specs[nspecs_done].info.width =
    	    args_value[specs[nspecs_done].width_arg].pa_int;
    	  if (specs[nspecs_done].info.width < 0)
    	    /* If the width value is negative left justification is
    	       selected and the value is taken as being positive.  */
    	    {
    	      specs[nspecs_done].info.width *= -1;
    	      left = specs[nspecs_done].info.left = 1;
    	    }
    	  width = specs[nspecs_done].info.width;
    	}
          if (specs[nspecs_done].prec_arg != -1)
    	{
    	  /* Extract the precision from an argument.  */
    	  specs[nspecs_done].info.prec =
    	    args_value[specs[nspecs_done].prec_arg].pa_int;
    	  if (specs[nspecs_done].info.prec < 0)
    	    /* If the precision is negative the precision is
    	       omitted.  */
    	    specs[nspecs_done].info.prec = -1;
    	  prec = specs[nspecs_done].info.prec;
    	}
          /* Process format specifiers.  */
          while (1)
    	{
    	  extern printf_function **__printf_function_table;
    	  int function_done;
    	  if (spec <= UCHAR_MAX
    	      && __printf_function_table != NULL
    	      && __printf_function_table[(size_t) spec] != NULL)
    	    {
    	      const void **ptr = alloca (specs[nspecs_done].ndata_args
    					 * sizeof (const void *));
    	      /* Fill in an array of pointers to the argument values.  */
    	      for (unsigned int i = 0; i < specs[nspecs_done].ndata_args;
    		   ++i)
    		ptr[i] = &args_value[specs[nspecs_done].data_arg + i];
    	      /* Call the function.  */
    	      function_done = __printf_function_table[(size_t) spec]
    		(s, &specs[nspecs_done].info, ptr);
    	      if (function_done != -2)
    		{
    		  /* If an error occurred we don't have information
    		     about # of chars.  */
    		  if (function_done < 0)
    		    {
    		      /* Function has set errno.  */
    		      done = -1;
    		      goto all_done;
    		    }
    		  done_add (function_done);
    		  break;
    		}
    	    }
    	  JUMP (spec, step4_jumps);
    #define process_arg_data args_value[specs[nspecs_done].data_arg]
    #define process_arg_int() process_arg_data.pa_int
    #define process_arg_long_int() process_arg_data.pa_long_int
    #define process_arg_long_long_int() process_arg_data.pa_long_long_int
    #define process_arg_pointer() process_arg_data.pa_pointer
    #define process_arg_string() process_arg_data.pa_string
    #define process_arg_unsigned_int() process_arg_data.pa_u_int
    #define process_arg_unsigned_long_int() process_arg_data.pa_u_long_int
    #define process_arg_unsigned_long_long_int() process_arg_data.pa_u_long_long_int
    #define process_arg_wchar_t() process_arg_data.pa_wchar
    #define process_arg_wstring() process_arg_data.pa_wstring
    	  process_arg ();
    	  process_string_arg ();
    #undef process_arg_data
    #undef process_arg_int
    #undef process_arg_long_int
    #undef process_arg_long_long_int
    #undef process_arg_pointer
    #undef process_arg_string
    #undef process_arg_unsigned_int
    #undef process_arg_unsigned_long_int
    #undef process_arg_unsigned_long_long_int
    #undef process_arg_wchar_t
    #undef process_arg_wstring
    	  LABEL (form_float):
    	  LABEL (form_floathex):
    	  {
    	    const void *ptr
    	      = (const void *) &args_value[specs[nspecs_done].data_arg];
    	    if (__glibc_unlikely ((mode_flags & PRINTF_LDBL_IS_DBL) != 0))
    	      {
    		specs[nspecs_done].data_arg_type = PA_DOUBLE;
    		specs[nspecs_done].info.is_long_double = 0;
    	      }
    	    SETUP_FLOAT128_INFO (specs[nspecs_done].info);
    	    int function_done
    	      = __printf_fp_spec (s, &specs[nspecs_done].info, &ptr);
    	    if (function_done < 0)
    	      {
    		/* Error in print handler; up to handler to set errno.  */
    		done = -1;
    		goto all_done;
    	      }
    	    done_add (function_done);
    	  }
    	  break;
    	  LABEL (form_unknown):
    	  {
    	    unsigned int i;
    	    const void **ptr;
    	    ptr = alloca (specs[nspecs_done].ndata_args
    			  * sizeof (const void *));
    	    /* Fill in an array of pointers to the argument values.  */
    	    for (i = 0; i < specs[nspecs_done].ndata_args; ++i)
    	      ptr[i] = &args_value[specs[nspecs_done].data_arg + i];
    	    /* Call the function.  */
    	    function_done = printf_unknown (s, &specs[nspecs_done].info,
    					    ptr);
    	    /* If an error occurred we don't have information about #
    	       of chars.  */
    	    if (function_done < 0)
    	      {
    		/* Function has set errno.  */
    		done = -1;
    		goto all_done;
    	      }
    	    done_add (function_done);
    	  }
    	  break;
    	}
          /* Write the following constant string.  */
          outstring (specs[nspecs_done].end_of_fmt,
    		 specs[nspecs_done].next_fmt
    		 - specs[nspecs_done].end_of_fmt);
        }
     all_done:
      scratch_buffer_free (&argsbuf);
      scratch_buffer_free (&specsbuf);
      return done;
    }
    
    /* Handle an unknown format specifier.  This prints out a canonicalized
       representation of the format spec itself.  */
    static int
    printf_unknown (FILE *s, const struct printf_info *info,
    		const void *const *args)
    {
      int done = 0;
      CHAR_T work_buffer[MAX (sizeof (info->width), sizeof (info->prec)) * 3];
      CHAR_T *const workend
        = &work_buffer[sizeof (work_buffer) / sizeof (CHAR_T)];
      CHAR_T *w;
      outchar (L_('%'));
      if (info->alt)
        outchar (L_('#'));
      if (info->group)
        outchar (L_('\''));
      if (info->showsign)
        outchar (L_('+'));
      else if (info->space)
        outchar (L_(' '));
      if (info->left)
        outchar (L_('-'));
      if (info->pad == L_('0'))
        outchar (L_('0'));
      if (info->i18n)
        outchar (L_('I'));
      if (info->width != 0)
        {
          w = _itoa_word (info->width, workend, 10, 0);
          while (w < workend)
    	outchar (*w++);
        }
      if (info->prec != -1)
        {
          outchar (L_('.'));
          w = _itoa_word (info->prec, workend, 10, 0);
          while (w < workend)
    	outchar (*w++);
        }
      if (info->spec != L_('\0'))
        outchar (info->spec);
     all_done:
      return done;
    }
    
    /* Group the digits from W to REAR_PTR according to the grouping rules
       of the current locale.  The interpretation of GROUPING is as in
       `struct lconv' from <locale.h>.  The grouped number extends from
       the returned pointer until REAR_PTR.  FRONT_PTR to W is used as a
       scratch area.  */
    static CHAR_T *
    group_number (CHAR_T *front_ptr, CHAR_T *w, CHAR_T *rear_ptr,
    	      const char *grouping, THOUSANDS_SEP_T thousands_sep)
    {
      /* Length of the current group.  */
      int len;
    #ifndef COMPILE_WPRINTF
      /* Length of the separator (in wide mode, the separator is always a
         single wide character).  */
      int tlen = strlen (thousands_sep);
    #endif
      /* We treat all negative values like CHAR_MAX.  */
      if (*grouping == CHAR_MAX || *grouping <= 0)
        /* No grouping should be done.  */
        return w;
      len = *grouping++;
      /* Copy existing string so that nothing gets overwritten.  */
      memmove (front_ptr, w, (rear_ptr - w) * sizeof (CHAR_T));
      CHAR_T *s = front_ptr + (rear_ptr - w);
      w = rear_ptr;
      /* Process all characters in the string.  */
      while (s > front_ptr)
        {
          *--w = *--s;
          if (--len == 0 && s > front_ptr)
    	{
    	  /* A new group begins.  */
    #ifdef COMPILE_WPRINTF
    	  if (w != s)
    	    *--w = thousands_sep;
    	  else
    	    /* Not enough room for the separator.  */
    	    goto copy_rest;
    #else
    	  int cnt = tlen;
    	  if (tlen < w - s)
    	    do
    	      *--w = thousands_sep[--cnt];
    	    while (cnt > 0);
    	  else
    	    /* Not enough room for the separator.  */
    	    goto copy_rest;
    #endif
    	  if (*grouping == CHAR_MAX
    #if CHAR_MIN < 0
    		   || *grouping < 0
    #endif
    		   )
    	    {
    	    copy_rest:
    	      /* No further grouping to be done.  Copy the rest of the
    		 number.  */
    	      w -= s - front_ptr;
    	      memmove (w, front_ptr, (s - front_ptr) * sizeof (CHAR_T));
    	      break;
    	    }
    	  else if (*grouping != '\0')
    	    len = *grouping++;
    	  else
    	    /* The previous grouping repeats ad infinitum.  */
    	    len = grouping[-1];
    	}
        }
      return w;
    }
    
    /* Helper "class" for `fprintf to unbuffered': creates a temporary buffer.  */
    struct helper_file
      {
        struct _IO_FILE_plus _f;
    #ifdef COMPILE_WPRINTF
        struct _IO_wide_data _wide_data;
    #endif
        FILE *_put_stream;
    #ifdef _IO_MTSAFE_IO
        _IO_lock_t lock;
    #endif
      };
    static int
    _IO_helper_overflow (FILE *s, int c)
    {
      FILE *target = ((struct helper_file*) s)->_put_stream;
    #ifdef COMPILE_WPRINTF
      int used = s->_wide_data->_IO_write_ptr - s->_wide_data->_IO_write_base;
      if (used)
        {
          size_t written = _IO_sputn (target, s->_wide_data->_IO_write_base, used);
          if (written == 0 || written == WEOF)
    	return WEOF;
          __wmemmove (s->_wide_data->_IO_write_base,
    		  s->_wide_data->_IO_write_base + written,
    		  used - written);
          s->_wide_data->_IO_write_ptr -= written;
        }
    #else
      int used = s->_IO_write_ptr - s->_IO_write_base;
      if (used)
        {
          size_t written = _IO_sputn (target, s->_IO_write_base, used);
          if (written == 0 || written == EOF)
    	return EOF;
          memmove (s->_IO_write_base, s->_IO_write_base + written,
    	       used - written);
          s->_IO_write_ptr -= written;
        }
    #endif
      return PUTC (c, s);
    }
    #ifdef COMPILE_WPRINTF
    static const struct _IO_jump_t _IO_helper_jumps libio_vtable =
    {
      JUMP_INIT_DUMMY,
      JUMP_INIT (finish, _IO_wdefault_finish),
      JUMP_INIT (overflow, _IO_helper_overflow),
      JUMP_INIT (underflow, _IO_default_underflow),
      JUMP_INIT (uflow, _IO_default_uflow),
      JUMP_INIT (pbackfail, (_IO_pbackfail_t) _IO_wdefault_pbackfail),
      JUMP_INIT (xsputn, _IO_wdefault_xsputn),
      JUMP_INIT (xsgetn, _IO_wdefault_xsgetn),
      JUMP_INIT (seekoff, _IO_default_seekoff),
      JUMP_INIT (seekpos, _IO_default_seekpos),
      JUMP_INIT (setbuf, _IO_default_setbuf),
      JUMP_INIT (sync, _IO_default_sync),
      JUMP_INIT (doallocate, _IO_wdefault_doallocate),
      JUMP_INIT (read, _IO_default_read),
      JUMP_INIT (write, _IO_default_write),
      JUMP_INIT (seek, _IO_default_seek),
      JUMP_INIT (close, _IO_default_close),
      JUMP_INIT (stat, _IO_default_stat)
    };
    #else
    static const struct _IO_jump_t _IO_helper_jumps libio_vtable =
    {
      JUMP_INIT_DUMMY,
      JUMP_INIT (finish, _IO_default_finish),
      JUMP_INIT (overflow, _IO_helper_overflow),
      JUMP_INIT (underflow, _IO_default_underflow),
      JUMP_INIT (uflow, _IO_default_uflow),
      JUMP_INIT (pbackfail, _IO_default_pbackfail),
      JUMP_INIT (xsputn, _IO_default_xsputn),
      JUMP_INIT (xsgetn, _IO_default_xsgetn),
      JUMP_INIT (seekoff, _IO_default_seekoff),
      JUMP_INIT (seekpos, _IO_default_seekpos),
      JUMP_INIT (setbuf, _IO_default_setbuf),
      JUMP_INIT (sync, _IO_default_sync),
      JUMP_INIT (doallocate, _IO_default_doallocate),
      JUMP_INIT (read, _IO_default_read),
      JUMP_INIT (write, _IO_default_write),
      JUMP_INIT (seek, _IO_default_seek),
      JUMP_INIT (close, _IO_default_close),
      JUMP_INIT (stat, _IO_default_stat)
    };
    #endif
    static int
    buffered_vfprintf (FILE *s, const CHAR_T *format, va_list args,
    		   unsigned int mode_flags)
    {
      CHAR_T buf[BUFSIZ];
      struct helper_file helper;
      FILE *hp = (FILE *) &helper._f;
      int result, to_flush;
      /* Orient the stream.  */
    #ifdef ORIENT
      ORIENT;
    #endif
      /* Initialize helper.  */
      helper._put_stream = s;
    #ifdef COMPILE_WPRINTF
      hp->_wide_data = &helper._wide_data;
      _IO_wsetp (hp, buf, buf + sizeof buf / sizeof (CHAR_T));
      hp->_mode = 1;
    #else
      _IO_setp (hp, buf, buf + sizeof buf);
      hp->_mode = -1;
    #endif
      hp->_flags = _IO_MAGIC|_IO_NO_READS|_IO_USER_LOCK;
    #if _IO_JUMPS_OFFSET
      hp->_vtable_offset = 0;
    #endif
    #ifdef _IO_MTSAFE_IO
      hp->_lock = NULL;
    #endif
      hp->_flags2 = s->_flags2;
      _IO_JUMPS (&helper._f) = (struct _IO_jump_t *) &_IO_helper_jumps;
      /* Now print to helper instead.  */
      result = vfprintf (hp, format, args, mode_flags);
      /* Lock stream.  */
      __libc_cleanup_region_start (1, (void (*) (void *)) &_IO_funlockfile, s);
      _IO_flockfile (s);
      /* Now flush anything from the helper to the S. */
    #ifdef COMPILE_WPRINTF
      if ((to_flush = (hp->_wide_data->_IO_write_ptr
    		   - hp->_wide_data->_IO_write_base)) > 0)
        {
          if ((int) _IO_sputn (s, hp->_wide_data->_IO_write_base, to_flush)
    	  != to_flush)
    	result = -1;
        }
    #else
      if ((to_flush = hp->_IO_write_ptr - hp->_IO_write_base) > 0)
        {
          if ((int) _IO_sputn (s, hp->_IO_write_base, to_flush) != to_flush)
    	result = -1;
        }
    #endif
      /* Unlock the stream.  */
      _IO_funlockfile (s);
      __libc_cleanup_region_end (0);
      return result;
    }
    ```
    

이 코드를 매번 짜는 사람은 없습니다.

C언어는 남이 만든 함수 코드를 내 코드에 집어넣을 수 있는 편리한 기능을 제공합니다.

이것을 “헤더파일” 이라고 부릅니다. 헤더파일은 남이 만든 코드입니다.

이 헤더파일을 포함시키는 #include 를 쓰면, 이 헤더파일에서 코딩한 함수를 모두 사용할 수 있습니다.

```c
#include <stdio.h>

int main(){
	puts("hello world!");
}
```

puts 는 내가 코딩한적 없는 함수인데도 쓸 수 있습니다.

c언어를 만든사람이 사람들 힘들지말라고, 미리 코딩해둔 것 입니다.

계속