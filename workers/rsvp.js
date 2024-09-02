addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  if (request.method === 'POST') {
    const data = await request.json();

    // Aqui você pode processar os dados de RSVP, incluindo o número de convidados
    const { name, email, guests } = data;
    console.log(`Nome: ${name}, Email: ${email}, Número de Convidados: ${guests}`);

    return new Response('RSVP recebido com sucesso!', { status: 200 });
  }

  return new Response('Método não permitido', { status: 405 });
}

