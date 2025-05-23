# 4-1_Cookie : Broken Access Control Mitigation

<aside>
💡 author : 전재호(agamtt) 2024-01-23

</aside>

# Broken Access Control Vulnerability

우리는 지난 시간까지 웹페이지를 만들고, 그것을 인터넷 상에 배포하고 접속할 수 있도록 개발해봤습니다.

웹페이지의 인증 기능은, 어떤 페이지를 접속하지 못하게 하거나, 접속할 때에 **인증**을 요구합니다.

그러나, 사용자가 개발자가 의도한대로만 제품을 사용할 것이라고 생각하면, 취약점이 발생합니다.

우리는 올바른 아이디와 비밀번호를 입력하여야만 개인페이지로 이동하도록 의도했습니다.

그러나, 개인페이지로 곧바로 이동해도 아무런 문제가 없었습니다.

특정 페이지나 기능을 사용할 때, 특정 사용자만 사용할 수 있게 하는 것을 개발에서 Access Control (접근 관리) 라고 부릅니다.

접근 관리에 결함이 있어서, 의도하지 않은 방법으로 접근을 허용하는 취약점을 Broken Access Control 이라고 합니다.

# Mitigation

이런 일이 발생하면 안되므로, 이것을 수정해야합니다.

취약점을 수정하여 보안을 강화하는 것을 완화(**Mitigation**) 이라고 부릅니다.

계속