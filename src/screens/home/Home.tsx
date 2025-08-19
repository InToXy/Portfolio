import {TypeAnimation} from 'react-type-animation';
import myImg from '../../assets/image_cv.png';

export const Home = () => {

  return (
    <div className="flex flex-col-reverse items-center justify-center sm:px-10 lg:pb-40 xl:flex-row xl:pb-0 xl:pt-20">
      <div className="flex w-full flex-col items-center py-10 text-xl xl:w-1/2 xl:items-end">
        <div className="w-fit">
          <p className="text-xl text-themePrimaryColor">
            <span className="span">{'<'}</span>Bonjour, je suis
          </p>

          <h1 className="pt-2 text-3xl font-bold text-primaryColor opacity-70 sm:text-5xl">
            Pinget Matheo <span className="text-3xl font-extrabold text-themePrimaryColor sm:text-5xl">{'/>'}</span>{' '}
          </h1>
          <TypeAnimation
            sequence={['Étudiant en Réseaux et Télécommunication', 1000, 'Technicien Réseaux', 1000, 'Spécialiste en Cybersécurité', 1000, 'Administrateur Systèmes et Réseaux', 1000]}
            wrapper="span"
            speed={1}
            style={{
              paddingTop: '8px',
              fontWeight: '300',
              fontSize: '1.5rem',
              color: '#768390',
              display: 'inline-block',
            }}
            repeat={Infinity}
          />
        </div>
      </div>
      <div className="static: w-ful top-0 flex justify-center xl:relative xl:top-[-64px] xl:w-1/2 xl:pt-10">
        <img
          className="h-[300px] w-[215px] md:h-[400px] md:w-[286px] xl:h-[500px] xl:w-[358px]"
          loading="lazy"
          src={myImg}
          alt="myPhoto"
        />
      </div>
    </div>
  );
};

export default Home;
