survey = {
  id: 1,
  desc: "grooming and personal hygiene",
  types: [
    {
      id: 1,
      desc: "personal hygiene",
      questions: [
        {
          id: 1,
          desc: "body odor",
          choice_id: 1,
        },
        {
          id: 2,
          desc: "shower taken",
        },
      ],
    },
    {
      id: 2,
      desc: "grooming",
      choice_type: {
        id: 1,
        desc: "radios",
        number_of_choices: 10,
      },
      questions: [
        {
          id: 1,
          desc: "clean shaved",
        },
        {
          id: 2,
          desc: "foundation applied",
        },
      ],
    },
  ],
};

answer = {
  employee: "mark guanzon",
  surveyor: "sadegh",
  survey: {},
};

response = {
  date: "date",
  id: 1,
  user_id: 1,
  survey_id: 1,
  answers: [
    {
      id: 1,
      answer: 9,
      question_id: 2,
      note: "forgot to take shower",
    },
  ],
};
