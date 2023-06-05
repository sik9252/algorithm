function solution(today, terms, privacies) {
  var answer = [];

  // 오늘 날짜를 년,월,일로 나눠서 저장
  const todayYear = +today.slice(0, 4);
  const todayMonth = +today.slice(5, 7);
  const todayDay = +today.slice(8, 10);

  // 약관 종류와 유효기간 저장
  const termsMap = {};
  for (const term of terms) {
    key = term.split(" ")[0];
    value = term.split(" ")[1];

    termsMap[key] = +value;
  }

  // 유효기간 더한 날짜를 반환하는 함수
  const checkDate = (year, month, exp) => {
    const testMonth = exp + month;
    let newYear =
      testMonth % 12 === 0
        ? year + parseInt(testMonth / 12) - 1
        : year + parseInt(testMonth / 12);
    let newMonth = testMonth % 12 === 0 ? 12 : testMonth % 12;

    return { year: newYear, month: newMonth };
  };

  // privacies
  for (let i = 0; i < privacies.length; i++) {
    const date = privacies[i].split(" ")[0];

    const termType = privacies[i].split(" ")[1];
    let year = +date.slice(0, 4);
    let month = +date.slice(5, 7);
    let day = +date.slice(8, 10);

    // 유효기간을 더한 날짜를 구하는 로직
    if (month + termsMap[termType] > 12) {
      year = checkDate(year, month, termsMap[termType]).year;
      month = checkDate(year, month, termsMap[termType]).month;
    } else {
      month = month + termsMap[termType];
    }

    // 오늘 날짜랑 비교
    if (todayYear > year) {
      answer.push(i + 1);
    } else if (todayYear === year) {
      if (todayMonth > month) {
        answer.push(i + 1);
      } else if (todayMonth === month) {
        if (todayDay >= day) {
          answer.push(i + 1);
        }
      }
    }
  }

  return answer;
}
