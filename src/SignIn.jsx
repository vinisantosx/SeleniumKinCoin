import React from "react";

function SignInForm() {
  const [state, setState] = React.useState({
    email: "",
    password: ""
  });

  const handleChange = evt => {
    const value = evt.target.value;
    setState({
      ...state,
      [evt.target.name]: value
    });
  };

  const handleOnSubmit = evt => {
    evt.preventDefault();

    const { email, password } = state;

    // Exibe feedback na tela, como o Selenium espera
    const feedback = document.getElementById("messageFeedback");

    if (!email.includes("@") || !email.includes(".")) {
      feedback.innerText = "Invalid format email!";
      return;
    }

    if (email === "test@example.com" && password === "123456789") {
      feedback.innerText =
        "Username and password correct, you will be redirect to adminsitrador page wait...";
    } else {
      feedback.innerText = "Invalid username or password!";
    }

    setState({ email: "", password: "" });
  };

  return (
    <div className="form-container sign-in-container">
      <form onSubmit={handleOnSubmit}>
        <h1>Login</h1>

        <span>Ou entre com sua conta</span>

        <input
          id="email"
          type="email"
          placeholder="Email"
          name="email"
          value={state.email}
          onChange={handleChange}
        />

        <input
          id="password"
          type="password"
          name="password"
          placeholder="Password"
          value={state.password}
          onChange={handleChange}
        />

        <button id="signin">Entrar</button>

        {/* Elemento esperado pelo Selenium */}
        <p id="messageFeedback" style={{ color: "red", marginTop: "10px" }}></p>
      </form>
    </div>
  );
}

export default SignInForm;
