import sys, os, getpass, cffi

ffi = cffi.FFI()
ffi.cdef( '''
  typedef unsigned char char_u;
  void bf_key_init( char_u *password, char_u *salt, int salt_len );
  void bf_cfb_init( char_u *iv, int iv_len );
  void bf_crypt_decode( char_u *ptr, long len );
''' )

blowfish = ffi.dlopen( os.path.join( os.path.dirname(__file__), 'blowfish.so' ) )

def decrypt( filename ):
  with open( filename ) as data:
    assert data.read(12) == 'VimCrypt~02!', 'input should be a vim-encrypted file'
    salt = data.read(8)
    seed = data.read(8)
    assert len(salt) == len(seed) == 8, 'data ended prematurely'
    buf = ffi.new( "unsigned char[]", data.read() )
  pw = getpass.getpass( 'password: ' )
  assert pw, 'empty password'
  blowfish.bf_key_init( pw, salt, len(salt) )
  blowfish.bf_cfb_init( seed, len(seed) )
  blowfish.bf_crypt_decode( buf, len(buf)-1 );
  return ffi.string( buf )

if __name__ == '__main__':
  if len(sys.argv) != 2:
    sys.exit( 'usage: %s [filename]' % os.path.basename(__file__) )
  print decrypt( sys.argv[1] )