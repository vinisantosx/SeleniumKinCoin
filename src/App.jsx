import React, { useState } from "react";
import "./styles.css";
import SignInForm from "./SignIn";
import SignUpForm from "./SignUp";

export default function App() {
  const [type, setType] = useState("signIn");

  const handleOnClick = (text) => {
    if (text !== type) {
      setType(text);
    }
  };

  // Classe que ativa/desativa o painel de cadastro
  const containerClass =
    "container " + (type === "signUp" ? "right-panel-active" : "");

  return (
    <div className="App">
      <div className={containerClass} id="container">
        
        {/* Formulário de Cadastro */}
        <SignUpForm />

        {/* Formulário de Login */}
        <SignInForm />

        {/* Painel deslizante */}
        <div className="overlay-container">
          <div className="overlay">

            {/* PAINEL DO SIGN IN */}
            <div className="overlay-panel overlay-left">
              <h1>Conecte-se conosco!</h1>
              <p>Já possui uma conta? Clique no botão abaixo.</p>

              <button
                className="ghost"
                id="signIn"
              >
                Fazer Login
              </button>
            </div>

            {/* PAINEL DO SIGN UP */}
            <div className="overlay-panel overlay-right">
              <h1>É um prazer te ver por aqui!</h1>
              <p>
                Não possui cadastro na nossa plataforma? Junte-se a nós clicando
                no botão abaixo.
              </p>

              <button
                className="ghost"
                id="signUp"
                onClick={() => handleOnClick("signUp")}
              >
                Sign Up
              </button>
            </div>

          </div>
        </div>

      </div>
    </div>
  );
}
