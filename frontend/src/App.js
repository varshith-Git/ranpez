import './App.css';
import Navbar from './Components/Navbar';
import Header from './Components/Header';
import Cards from './Components/Cards';
import Trusted from './Components/Trusted';
import FAQs from './Components/FAQs';
import Footer from './Components/Footer';

function App() {
  return (
    <div>
     <Navbar/>
     <Header/>
     <Cards/>
     <Trusted/>
     <FAQs/>
     <Footer/>
    </div>
  );
}

export default App;
