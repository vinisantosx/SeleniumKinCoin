import React from "react";

// Função para validar telefone: (11) 91234-5678
function isValidPhone(phone) {
  const regex = /^\(\d{2}\) 9\d{4}-\d{4}$/;
  return regex.test(phone);
}

// Função para validar email
function isValidEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

// Função para validar CPF
function isValidCPF(cpf) {
  cpf = cpf.replace(/[.-]/g, "");

  if (cpf.length !== 11 || /^(\d)\1+$/.test(cpf)) return false;

  let soma = 0;
  for (let i = 0; i < 9; i++) soma += parseInt(cpf[i]) * (10 - i);
  let digito1 = (soma * 10) % 11;
  if (digito1 === 10) digito1 = 0;
  if (digito1 !== parseInt(cpf[9])) return false;

  soma = 0;
  for (let i = 0; i < 10; i++) soma += parseInt(cpf[i]) * (11 - i);
  let digito2 = (soma * 10) % 11;
  if (digito2 === 10) digito2 = 0;
  return digito2 === parseInt(cpf[10]);
}

function SignUpForm() {
  const [state, setState] = React.useState({
    name: "",
    phone: "",
    cpf: "",
    email: "",
    confirmEmail: "",
    password: "",
    confirmpassword: ""
  });

  const handleChange = evt => {
    setState({
      ...state,
      [evt.target.name]: evt.target.value
    });
  };

  const handleOnSubmit = evt => {
    evt.preventDefault();

    const {
      name,
      phone,
      cpf,
      email,
      confirmEmail,
      password,
      confirmpassword
    } = state;

    const feedback = document.getElementById("signupMessage");

    // Nome vazio
    if (name.trim() === "") {
      feedback.innerText = "Name cannot be empty!";
      return;
    }

    // Telefone
    if (!isValidPhone(phone)) {
      feedback.innerText = "Invalid phone format!";
      return;
    }

    // CPF
    if (!isValidCPF(cpf)) {
      feedback.innerText = "Invalid CPF!";
      return;
    }

    // Email
    if (!isValidEmail(email)) {
      feedback.innerText = "Invalid email format!";
      return;
    }

    // Confirmar email
    if (email !== confirmEmail) {
      feedback.innerText = "Emails do not match!";
      return;
    }

    // Senha mínima
    if (password.length < 8) {
      feedback.innerText = "Password must contain at least 8 characters!";
      return;
    }

    // Confirmar senha
    if (password !== confirmpassword) {
      feedback.innerText = "Passwords do not match!";
      return;
    }

    // Sucesso
    feedback.innerText = "Account created successfully!";

    setState({
      name: "",
      phone: "",
      cpf: "",
      email: "",
      confirmEmail: "",
      password: "",
      confirmpassword: ""
    });
  };

  return (
    <div className="form-container sign-up-container">
      <form onSubmit={handleOnSubmit}>
        <h1>Criar Conta</h1>

        <input
          id="signup_name"
          type="text"
          name="name"
          value={state.name}
          onChange={handleChange}
          placeholder="Nome completo"
        />

        <input
          id="signup_telefone"
          type="text"
          name="phone"
          value={state.phone}
          onChange={handleChange}
          placeholder="(11) 91234-5678"
        />

        <input
          id="signup_cpf"
          type="text"
          name="cpf"
          value={state.cpf}
          onChange={handleChange}
          placeholder="123.456.789-09"
        />

        <input
          id="signup_email"
          type="email"
          name="email"
          value={state.email}
          onChange={handleChange}
          placeholder="Email"
        />

        <input
          id="signup_confirm_email"
          type="email"
          name="confirmEmail"
          value={state.confirmEmail}
          onChange={handleChange}
          placeholder="Confirmar Email"
        />

        <input
          id="signup_password"
          type="password"
          name="password"
          value={state.password}
          onChange={handleChange}
          placeholder="Senha"
        />

        <input
          id="signup_confirm_password"
          type="password"
          name="confirmpassword"
          value={state.confirmpassword}
          onChange={handleChange}
          placeholder="Confirmar Senha"
        />

        <button id="signup_button">Cadastre-se</button>

        <p id="signupMessage" style={{ color: "red", marginTop: "10px" }}></p>
      </form>
    </div>
  );
}

export default SignUpForm;
